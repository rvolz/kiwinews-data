from dotenv import load_dotenv
from pathlib import Path
import click
from dune_client.client import DuneClient
from dotenv import load_dotenv

load_dotenv()


DUNE_TABLES = {
    'tips': { 'name': 'kiwi_news_tips', 'description': 'Kiwi news tip data'},
    'activities': { 'name': 'kiwi_news_activities', 'description': 'Kiwi news user activities per month'},
    'stories': { 'name': 'kiwi_news_stories', 'description': 'Kiwi news top stories per month'},
}

@click.command()
@click.option("--file_name", required=True, help="CSV file")
@click.option("--kind", required=True, help="activities|stories|tips")
def upload_file(file_name, kind):
    with open(file_name) as f:
        csv_data = f.read()
    dune = DuneClient.from_env()
    table_data = DUNE_TABLES[kind]
    res = dune.upload_csv(table_name = table_data['name'], data = csv_data, description = table_data['description'])
    if not res:
        exit(1)

if __name__ == '__main__':
    upload_file()

