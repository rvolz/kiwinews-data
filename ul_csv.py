from dotenv import load_dotenv
from pathlib import Path
import click
from dune_client.client import DuneClient
from dotenv import load_dotenv

load_dotenv()


DUNE_TABLES = {
    'tip_receivers': { 'name': 'kiwi_news_tiprecs', 'description': 'Kiwi news tip receivers'},
    'tip_senders': { 'name': 'kiwi_news_tippers', 'description': 'Kiwi news tip senders'},
    'activities': { 'name': 'kiwi_news_activities', 'description': 'Kiwi news user activities per month'},
    'stories': { 'name': 'kiwi_news_stories', 'description': 'Kiwi news top stories per month'},
}

@click.command()
@click.option("--file_name", required=True, help="CSV file")
@click.option("--kind", required=True, help="tip_sender|tip_receiver|activities")
def upload_file(file_name, kind):
    with open(file_name) as f:
        csv_data = f.read()
    print(csv_data)
    dune = DuneClient.from_env()
    table_data = DUNE_TABLES[kind]
    res = dune.upload_csv(table_name = table_data['name'], data = csv_data, description = table_data['description'])
    if not res:
        exit(1)

if __name__ == '__main__':
    upload_file()

