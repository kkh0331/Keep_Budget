import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

db = pymysql.connect(
        host=os.environ.get("FLASK_DB_HOST"),
        port=int(os.environ.get("FLASK_DB_PORT")),
        user=os.environ.get("FLASK_DB_USER"),
        password=os.environ.get("FLASK_DB_PASSWORD"),
        db=os.environ.get("FLASK_DB_NAME"),
        charset='utf8'
    )

cursor = db.cursor()

# SQL query 작성
sql = """CREATE TABLE real_state_news(
         id  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         date VARCHAR(32),
         title TEXT,
         url TEXT,
         img_url Text,
         summary Text,
         종로구 INT,
         중구 INT,
         용산구 INT,
         성동구 INT,
         광진구 INT,
         동대문구 INT,
         중랑구 INT,
         성북구 INT,
         강북구 INT,
         도봉구 INT,
         노원구 INT,
         은평구 INT,
         서대문구 INT,
         마포구 INT,
         양천구 INT,
         강서구 INT,
         구로구 INT,
         금천구 INT,
         영등포구 INT,
         동작구 INT,
         관악구 INT,
         서초구 INT,
         강남구 INT,
         송파구 INT,
         강동구 INT,
         인천 INT,
         수원 INT,
         고양 INT,
         성남 INT,
         부천 INT,
         화성 INT,
         안산 INT,
         남양주 INT,
         안양 INT,
         평택 INT,
         시흥 INT,
         파주 INT,
         의정부 INT,
         김포 INT,
         광주 INT,
         광명 INT,
         군포 INT,
         하남 INT,
         오산 INT,
         양주 INT,
         이천 INT,
         구리 INT,
         안성 INT,
         포천 INT,
         의왕 INT,
         양평 INT,
         여주 INT,
         동두천 INT,
         가평 INT,
         과천 INT,
         연천 INT,
         용인 INT,
         중립 DOUBLE,
         긍정 DOUBLE,
         부정 DOUBLE,
         최종 VARCHAR(16)
         );"""

cursor.execute(sql)

cursor.execute("show tables")

db.commit()

db.close()