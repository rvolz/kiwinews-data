import json
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import click

load_dotenv()

data_dir = Path("./data")
if not data_dir.exists():
    data_dir.mkdir(parents=True)


@click.command()
def download_tips():    
    url = os.getenv("TIPS_API")
    token = os.getenv("TIPS_TOKEN")
    
    response = requests.get(url=url, headers = {"Authorization": f"Bearer {token}"})
    if response.ok:
        with open("data/tips.json", "w") as f:
            f.write(json.dumps(response.json()))
    else:
        print(response)

if __name__ == '__main__':
    download_tips()

