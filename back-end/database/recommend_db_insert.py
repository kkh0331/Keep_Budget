# -*- coding: utf-8 -*-
import sys
import os
import pymysql
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

db = pymysql.connect(
    host=os.environ.get("FLASK_DB_HOST"),
    port=int(os.environ.get("FLASK_DB_PORT")),
    user=os.environ.get("FLASK_DB_USER"),
    password=os.environ.get("FLASK_DB_PASSWORD"),
    db=os.environ.get("FLASK_DB_NAME"),
    charset='utf8'
)

df = pd.read_csv('./오피스텔_전세.csv')

for index, row in df.iterrows():
    try:
        cursor = db.cursor()
        sql = f"INSERT INTO recommend(region, addr, x_coordinate, y_coordinate, name, price, floor, size, house, type) VALUES('{row['region']}', '{row['addr']}', {row['x_coordinate']}, {row['y_coordinate']}, '{row['name']}', {row['price']}, {row['floor']}, {row['size']}, '{row['house']}', '{row['type']}');"
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        continue
# 접속 종료
db.close()