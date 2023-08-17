from flask import Flask
from real_state_routes import real_state_routes
from accident_routes import accident_routes
from apscheduler.schedulers.background import  BackgroundScheduler
from datetime import datetime, timedelta

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sub_script_path = os.path.join(parent_dir, "database", "real_state_news_db_insert.py")
sys.path.append(parent_dir)
from database.real_state_news_db_insert import real_state_news_crawling_to_db_insert

app = Flask(__name__)

# scheduler 설정한 시간이 되면 자동적으로 크롤링 진행해 db에 저장 - but 잠시 주석 처리
# def yesterday_news_crawling():
#     current_date = datetime.now()
#     one_day_ago = current_date - timedelta(days=1)
#     previous_month = one_day_ago.month
#     previous_day = one_day_ago.day
#     print(f'{previous_month}월 {previous_day}일의 뉴스 db 저장 시작')
#     real_state_news_crawling_to_db_insert(previous_month, previous_day, previous_month, previous_day, 101, 260)
#     # 원래는 db 내용을 같이 받아 오려고 했으나 flask 실행을 하고 있을 때 켜면 jvm 문제가 발생을 하여 database > accident_news_db_insert.py에서 따로 실행
#     # accident_news_crawling_to_db_insert(previous_month, previous_day, previous_month, previous_day, 102, 249)
#     print(f'{previous_month}월 {previous_day}일의 뉴스 db 저장 완료')

# scheduler = BackgroundScheduler()
# scheduler.add_job(yesterday_news_crawling, 'cron', hour=2) # 오전 2시에 전날 뉴스 기사 가져옴
# scheduler.start()

app.register_blueprint(real_state_routes)
app.register_blueprint(accident_routes)

if __name__ == '__main__':
    app.run()