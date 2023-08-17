from flask import Blueprint, request, jsonify
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

real_state_routes = Blueprint('real_state_routes', __name__)

@real_state_routes.route('/real_state_news_chart', methods = ['POST'])
def real_state_news_graph():
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
            sql = f"SELECT DISTINCT * FROM real_state_news WHERE {region} > 0"
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            sentiment_ratio = {"neutrality": 0, "positive": 0, "negative": 0}
            for row in results:
                sentiment_ratio["neutrality"] += row[63]
                sentiment_ratio["positive"] += row[64]
                sentiment_ratio["negative"] += row[65]
            return jsonify(sentiment_ratio)
        except Exception as e:
            return jsonify({"error" : str(e)})

@real_state_routes.route('/real_state_news_element', methods = ['POST'])
def real_state_news_element():
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
            item = request.json.get('selected_item')
            cursor = db.cursor()
            sql = f"SELECT DISTINCT  * FROM real_state_news WHERE {region} > 0 and 최종 = '{item}' ORDER BY {item} DESC "
            cursor.execute(sql)
            results = cursor.fetchmany(10)
            cursor.close()
            db.close()
            news_list = []
            for row in results:
                news_item = {
                    "date": row[1],
                    "title": row[2],
                    "url": row[3],
                    "img_url": row[4],
                    "summary": row[5],
                    "neutrality": row[63],
                    "positive": row[64],
                    "negative": row[65],
                    "final": row[66]
                }
                news_list.append(news_item)
            return jsonify(news_list)
        except Exception as e:
            return jsonify({"error" : str(e)})