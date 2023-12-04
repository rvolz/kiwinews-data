from pathlib import Path
from datetime import date
from urllib.parse import urlparse
import jsonlines
import csv
import click
import pandas as pd

@click.command()
@click.option("--limit", required=True, help="ISO date (YYYY-mm-dd) limit, normally the last day of the month")
@click.option("--nr_stories", default=5, help="Number of top stories to get")
def get_top_stories(limit, nr_stories):
    date_limit = date.fromisoformat(limit)
    click.echo(f"Getting top stories for range <= {date_limit}")
    # Create table from JSON
    with open('data/stories.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["date","href","title"])
        for p in sorted(Path("./data").glob("*.jsonl")):
            with jsonlines.open(p) as reader:
                for row in reader:
                    dt = date.fromtimestamp(row["timestamp"])
                    if dt < date_limit:
                        # Get rid of query parameters in the URL before exporting
                        u = urlparse(row["href"])
                        nurl = f'{u.scheme}://{u.hostname}{u.path}'
                        writer.writerow([dt.isoformat(), nurl, row["title"]])
    # Aggregate stories and export the top stories per month
    stories = pd.read_csv('./data/stories.csv',parse_dates=['date'])
    stories = stories.assign(
        year=lambda x: x.date.dt.year,
        month=lambda x: x.date.dt.month,
        )
    stories['ym'] = stories.date.apply(lambda x: x.strftime('%Y-%m'))
    stories = stories.drop(stories[(stories.year == 2023) & (stories.month < 9 )].index)
    top_stories_per_month = stories[['year','month', 'href', 'title', 'ym']].groupby(by=['year', 'month'],as_index=False).value_counts(sort=True,ascending=False)
    top_stories = top_stories_per_month.groupby(["year", "month"]).head(nr_stories)
    top_stories.to_csv('./data/top_stories.csv', header=True, index=False,columns=['ym','href','title', 'count'])

if __name__ == '__main__':
    get_top_stories()
