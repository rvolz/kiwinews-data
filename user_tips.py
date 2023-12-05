from pathlib import Path
from datetime import date
import json
import csv
import click

@click.command()
def user_tips():
    with open('./data/tips.json') as f:
           tips = json.load(f)
    with open('./data/kiwi_news_tips.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["user", "role", "amount", "count"])
        recs = tips['data']['receivers']
        for rec in recs.keys():
            writer.writerow([rec, 1, recs[rec]['totalValue'], recs[rec]['count']])
        recs = tips['data']['tippers']
        for rec in recs.keys():
            writer.writerow([rec, 2, recs[rec]['totalValue'], recs[rec]['count']])

if __name__ == '__main__':
    user_tips()

