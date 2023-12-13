#!/bin/bash
source .venv/bin/activate
date >> tips-update.log
python dl_tips.py >> tips-update.log
python user_tips.py >> tips-update.log
python ul_csv.py --file_name data/kiwi_news_tips.csv --kind tips >> tips-update.log
python refresh.py --kind tips >> tips-update.log
