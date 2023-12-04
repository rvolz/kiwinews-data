import requests
import jsonlines
import os
from dotenv import load_dotenv
from pathlib import Path
import click

load_dotenv()


data_dir = Path("./data")
if not data_dir.exists():
    data_dir.mkdir(parents=True)

@click.command()
@click.option("--start", default=0, help="Start index for message downloads. Set to 0 to get all.")
def download_messages(start):
    # Get the Kiwi News API URL for messages
    url = os.getenv("KIWI_MESSAGES_API")
    # Page length
    rows = 100

    index = start
    while True:
        click.echo(f"requesting {rows} messages, starting at {index}", color=True)
        response = requests.post(url=url,json={"from": index, "amount": rows })
        if response.status_code == 200:
            r = response.json()
            if len(r["data"]) == 0:
                break
            with jsonlines.open(f'./data/messages-{index:04d}.jsonl', mode='w') as writer:
                writer.write_all(r["data"])
            index += rows
            click.echo("messages downloaded", color = True)
        else:
            click.echo(response, err=True, color=True)
            break

if __name__ == '__main__':
    download_messages()
