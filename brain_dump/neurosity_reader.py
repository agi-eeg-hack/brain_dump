from csv import DictReader
from io import TextIOWrapper
import json
import os
from pathlib import Path
from typing import Callable, Generator, Iterator, NamedTuple
from .neurosity_types import NeurosityDatapoint, NeurosityDatasetMeta

import cattrs


class NeurosityCSVReader(DictReader):
    def __init__(self, file: TextIOWrapper) -> None:
        super().__init__(
            file,
            fieldnames=[
                "unknown1",
                "channel_1",
                "channel_2",
                "channel_3",
                "channel_4",
                "channel_5",
                "channel_6",
                "channel_7",
                "channel_8",
                "unknown2",
                "timestamp_sec",
            ],
        )

    def __next__(self):
        next = super().__next__()
        return cattrs.structure(next, NeurosityDatapoint)


class NeurosityDataset(NamedTuple):
    name: str
    path: str
    meta: NeurosityDatasetMeta | None


def datasets_in_parent(root_path: Path) -> Generator[NeurosityDataset, None, None]:
    for dirstr, _, filenames in os.walk(root_path):
        meta = None
        dirpath = Path(dirstr)

        if "dataset-metadata.json" in filenames:
            with open(dirpath / "dataset-metadata.json") as meta_file:
                meta = cattrs.structure(json.load(meta_file), NeurosityDatasetMeta)
        if "dataset.csv" in filenames:
            yield NeurosityDataset(
                name=dirpath.name,
                path=dirpath / "dataset.csv",
                meta=meta,
            )


def process_datasets_in_parent(
    root_path: Path,
    callback: Callable[[NeurosityDataset, Iterator[NeurosityDatapoint]], None],
):
    for dataset in datasets_in_parent(root_path):
        if dataset.meta.valid:
            with open(dataset.path, "r") as f:
                callback(dataset, NeurosityCSVReader(f))
