from flask import Blueprint, request, jsonify
import pymysql
from collections import Counter
import os
from dotenv import load_dotenv

load_dotenv()

accident_routes = Blueprint('accident_routes', __name__)

@accident_routes.route('/accident_news', methods = ['POST'])
def accident_routes_news():
    if request.method == 'POST':
        try:
            db = pymysql.connect(
                host=os.environ.get("FLASK_DB_HOST"),
                port=int(os.environ.get("FLASK_DB_PORT")),
                user=os.environ.get("FLASK_DB_USER"),
                password=os.environ.get("FLASK_DB_PASSWORD"),
                db=os.environ.get("FLASK_DB_NAME"),
                charset='utf8'
            )
            region = request.json.get('move_region')
            cursor = db.cursor()
            sql = f"SELECT DISTINCT * FROM accident_news WHERE {region} > 0 ORDER BY date DESC"
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            news_list = []
            morphology_list = []
            for row in results:
                news_item = {
                    "date": row[1],
                    "title": row[2],
                    "url": row[3],
                    "img_url": row[4],
                    "summary": row[5]
                }
                morphology_list.extend(row[6].split())
                news_list.append(news_item)
            counts = Counter(morphology_list)
            tags = counts.most_common(20)
            tag_list = []
            for tag in tags:
                tag_item = {
                    "text" : tag[0],
                    "value" : tag[1]
                }
                tag_list.append(tag_item)
            data = {'wordCloudData' : tag_list, 'accidentNewsData' : news_list}
            return jsonify(data)
        except Exception as e:
            return jsonify({"error" : str(e)})

