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
sql = """CREATE TABLE recommend(
         id  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         regrion Text,
         addr Text,
         x_coordinate Double,
         y_coordinate Double,
         name Text,
         price Double,
         floor Int,
         size Double,
         house Text,
         type Text
         );"""

cursor.execute(sql)

cursor.execute("show tables")

db.commit()

db.close()