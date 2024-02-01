#!/bin/bash
set -e
source .venv/bin/activate
date >> tips-update.log
python dl_tips.py >> tips-update.log 2>&1
python user_tips.py >> tips-update.log 2>&1
python ul_csv.py --file_name data/kiwi_news_tips.csv --kind tips >> tips-update.log 2>&1
python refresh.py --kind tips >> tips-update.log 2>&1
