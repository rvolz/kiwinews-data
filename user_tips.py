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
        rec_amount = tip_amount = rec_ctr = tip_ctr= 0
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["user", "role", "amount", "count"])
        recs = tips['data']['receivers']
        for rec in recs.keys():
            amount = round(recs[rec]['totalValue'],2)
            count = recs[rec]['count']
            rec_amount += amount
            rec_ctr += count
            writer.writerow([rec, 'receiver', amount, count])
        recs = tips['data']['tippers']
        for rec in recs.keys():
            amount = round(recs[rec]['totalValue'],2)
            count = recs[rec]['count']
            tip_amount += amount
            tip_ctr += count
            writer.writerow([rec, 'tipper', amount, count])
    if round(rec_amount,2) != round(tip_amount,2) or rec_ctr != tip_ctr:
        click.echo(f"sums don't add up: amounts ({rec_amount}/{tip_amount}), counters ({rec_ctr}/{tip_ctr})", err=True)        
        exit(1) 
    else:
        exit(0)


if __name__ == '__main__':
    user_tips()

