# -*- coding: utf-8 -*-
import sys
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sentiment_analysis import final_before_database

def real_state_news_crawling_to_db_insert(startMonth, startDay, endMonth, endDay, id1, id2):
    db = pymysql.connect(
        host=os.environ.get("FLASK_DB_HOST"),
        port=int(os.environ.get("FLASK_DB_PORT")),
        user=os.environ.get("FLASK_DB_USER"),
        password=os.environ.get("FLASK_DB_PASSWORD"),
        db=os.environ.get("FLASK_DB_NAME"),
        charset='utf8'
    )
    df = final_before_database(startMonth, startDay, endMonth, endDay, id1, id2)
    for index, row in df.iterrows():
        try:
            cursor = db.cursor()
            sql = f"INSERT INTO real_state_news(date, title, url, img_url, summary, 종로구, 중구, 용산구, 성동구, 광진구, 동대문구, 중랑구, 성북구, 강북구, 도봉구, 노원구, 은평구, 서대문구, 마포구, 양천구, 강서구, 구로구, 금천구, 영등포구, 동작구, 관악구, 서초구, 강남구, 송파구, 강동구, 인천, 수원, 고양, 성남, 부천, 화성, 안산, 남양주, 안양, 평택, 시흥, 파주, 의정부, 김포, 광주, 광명, 군포, 하남, 오산, 양주, 이천, 구리, 안성, 포천, 의왕, 양평, 여주, 동두천, 가평, 과천, 연천, 용인, 중립, 긍정, 부정, 최종) VALUES('{row['date']}', '{row['title']}', '{row['url']}', '{row['img_url']}', '{row['summary']}', {row['종로구']}, {row['중구']}, {row['용산구']}, {row['성동구']}, {row['광진구']}, {row['동대문구']}, {row['중랑구']}, {row['성북구']}, {row['강북구']}, {row['도봉구']}, {row['노원구']}, {row['은평구']}, {row['서대문구']}, {row['마포구']}, {row['양천구']}, {row['강서구']}, {row['구로구']}, {row['금천구']}, {row['영등포구']}, {row['동작구']}, {row['관악구']}, {row['서초구']}, {row['강남구']}, {row['송파구']}, {row['강동구']}, {row['인천']}, {row['수원']}, {row['고양']}, {row['성남']}, {row['부천']}, {row['화성']}, {row['안산']}, {row['남양주']}, {row['안양']}, {row['평택']}, {row['시흥']}, {row['파주']}, {row['의정부']}, {row['김포']}, {row['광주']}, {row['광명']}, {row['군포']}, {row['하남']}, {row['오산']}, {row['양주']}, {row['이천']}, {row['구리']}, {row['안성']}, {row['포천']}, {row['의왕']}, {row['양평']}, {row['여주']}, {row['동두천']}, {row['가평']}, {row['과천']}, {row['연천']}, {row['용인']}, {row['중립']}, {row['긍정']}, {row['부정']}, '{row['최종']}');"
            cursor.execute(sql)
            db.commit()
        except:
             continue
    # 접속 종료
    db.close()