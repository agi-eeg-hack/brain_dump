# Setup

Install neurosity in parent dir

```
cd ../ # relative to this repo
git clone https://github.com/neurosity/neurosity-sdk-python
```

Install this repo

```
python -m venv .venv --prompt brain_dump # Use python 3.11 (others at own risk)
. ./venv/bin/activate
pip install pip-tools
pip-sync
```

# Reading neurosity data

## Everything in a parent dir

```
def process_datapoint(
        dataset: NeurosityDataset, data: Iterator[NeurosityDatapoint]
) -> None:
    print(f"Processing {dataset.name} of subject {dataset.meta.anonymousSubjectId}")
    for datum in window(data, 10):
        print(datum)

process_datasets_in_parent(
    Path("/Users/lund/Documents/sessions/"), process_datapoint
)
```

## A specific file

```
with open(
    "/Users/lund/Documents/sessions/vEmgKzwF9WVEYvF8IQxC/dataset.csv", "r"
) as f:
    reader = NeurosityCSVReader(f)
    for row in window(reader, 10):
        print(row)
```
