from typing import Any
from attr import define
from datetime import datetime


@define
class NeurosityDatapoint:
    unknown1: int
    channel_1: float
    channel_2: float
    channel_3: float
    channel_4: float
    channel_5: float
    channel_6: float
    channel_7: float
    channel_8: float
    unknown2: Any
    timestamp_sec: float

    @property
    def python_timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp_sec)


@define
class NeurosityDatasetMeta:
    modelId: str
    id: str
    name: str
    timestamp: str
    label: str
    experimentId: str
    metric: str
    sessionId: str
    duration: int
    storagePath: str
    type: str
    anonymousSubjectId: str

    @property
    def python_timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp)

    @property
    def valid(self) -> bool:
        # So we can easily filter out datasets that are not of interest
        return True
