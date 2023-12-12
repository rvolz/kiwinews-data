from dotenv import load_dotenv
from pathlib import Path
import click
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase
from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option("--kind", required=True, help="tips")
def refresh(kind):
    if kind == 'tips':
        query = QueryBase(
            name="Kiwi News Tips Total",
            query_id=3259924,
            params=[],
        )
    else:
        click.echo(f'invalid parameter {kind}', err=True)
    dune = DuneClient.from_env()
    results = dune.run_query(query)


if __name__ == '__main__':
    refresh()

