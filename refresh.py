from dotenv import load_dotenv
from pathlib import Path
import click
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option("--kind", required=True, help="tip_sender|tip_receiver|activities")
def refresh(kind):
    query = QueryBase(
        name="Kiwi News top stories per month",
        query_id=3246050,
        params=[],
    )
    dune = DuneClient.from_env()
    results = dune.run_query(query)


if __name__ == '__main__':
    refresh()

