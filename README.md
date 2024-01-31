# Kiwi News data analysis

Scripts and notebooks to maintain the [Dune analysis page](https://dune.com/rvolz/kiwi-news) for the decentralized crypto news [Kiwi News](https://news.kiwistand.com/).

## Setup

Create a virtualenv for Python:

```sh
python -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt
```

## Usage

Download message data from a Kiwi News instance for analysis:

```sh
python dl_messages.py
```

This will create JSONL files in the `data` directory. If there is already data, consider using the start index to avoid a new download:

```sh
python dl_messages.py --start 6100
```

Get active users per month:

```sh
python user_activity.py --limit 2023-11-30
```

Get the top stories per month:

```sh
python top_stories.py --limit 2023-11-30
```

The resulting files can then be uploaded to Dune.
