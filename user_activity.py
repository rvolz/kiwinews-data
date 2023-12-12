from pathlib import Path
from datetime import date
import jsonlines
import csv
import click

@click.command()
@click.option("--limit", required=True, help="ISO date (YYYY-mm-dd) limit, normally the last day of the month")
def user_activity(limit):
    date_limit = date.fromisoformat(limit)
    click.echo(f"Getting user activity <= {date_limit}")
    with open('./data/kiwi_news_activity.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["date","user"])
        for p in sorted(Path("./data").glob("*.jsonl")):
            with jsonlines.open(p) as reader:
                for row in reader:
                    dt = date.fromtimestamp(row["timestamp"])
                    if dt <= date_limit:
                        writer.writerow([dt.isoformat(),row["identity"]])


if __name__ == '__main__':
    user_activity()

