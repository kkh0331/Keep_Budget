import os
import pymysql
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

region = "강동구".replace('"', '')

sql = f"SELECT * FROM accident_news where 관악구 > 0"

cursor.execute(sql)
results = cursor.fetchall()

# news_list = []
# for row in results:
#     news_item = {
#         "date" : row[1],
#         "title" : row[2],
#         "url" : row[3],
#         "img_url" : row[4],
#         "summary" : row[5],
#         "neutrality": row[63],
#         "positive": row[64],
#         "negative" : row[65],
#         "final": row[66]
#     }
#     news_list.append(news_item)
#
# for new_item in news_list:
#     # if new_item["final"] != "긍정":
#     #     continue
#     print(new_item)
print(len(results))

cursor.close()
db.close()