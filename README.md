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
