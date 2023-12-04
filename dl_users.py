import requests
import csv
import os
from dotenv import load_dotenv
from pathlib import Path
import click

load_dotenv()

data_dir = Path("./data")
if not data_dir.exists():
    data_dir.mkdir(parents=True)

@click.command()
def download_users():
    # Get the Kiwi News API URL for users
    url = os.getenv("KIWI_USERS_API")
    response = requests.get(url=url)
    if response.status_code == 200:
        r = response.json()
        with open('./data/users.csv', mode='w') as csvfile:
            writer = csv.writer(csvfile)
            for u in r["data"]:
                writer.writerow([u])
        click.echo("users downloaded", color = True)
    else:
        click.echo(response, color = True, err = True)


if __name__ == '__main__':
    download_users()
