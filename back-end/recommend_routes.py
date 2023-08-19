from flask import Blueprint, request, jsonify
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

recommend_routes = Blueprint('recommend_routes', __name__)

weights = {
    'x_coordinate': 1.2,
    'y_coordinate': 1.2,
    'price': 1,
    'size': 1,
}

@recommend_routes.route('/recommend', methods = ['POST'])
def recommend_list():
    if request.method == 'POST':
        try:
            user_info = request.json.get('user_info')
            want_move_region = request.json.get('want_move_region')
            user = user_info_change(user_info, want_move_region)
            db = pymysql.connect(
                host=os.environ.get("FLASK_DB_HOST"),
                port=int(os.environ.get("FLASK_DB_PORT")),
                user=os.environ.get("FLASK_DB_USER"),
                password=os.environ.get("FLASK_DB_PASSWORD"),
                db=os.environ.get("FLASK_DB_NAME"),
                charset='utf8'
            )
            cursor = db.cursor()
            sql = f"SELECT DISTINCT * FROM recommend WHERE house='{user['moveHouse']}' and type='{user['moveHouseType']}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            db.close()
            data = []
            for item in results:
                if int(float(item[6])) > user['collectMoney'] * 1.3 or int(float(item[8])) > user['moveSize']*1.3:
                    continue
                loan_price = 0
                if user['collectMoney'] < int(float(item[6])):
                    loan_price = int(float(item[6])) - user['collectMoney']
                new_item = {
                    'addr' : item[2],
                    'x_coordinate' : item[3],
                    'y_coordinate' : item[4],
                    'name' : item[5],
                    'price' : item[6],
                    'floor' : item[7],
                    'size' : item[8],
                    'id' : item[0],
                    'loan' : loan_price
                }
                data.append(new_item)
            user_coordinate = change_region_coordinate(user['moveRegion'])
            user_input = {
                'x_coordinate' : user_coordinate[0],
                'y_coordinate' : user_coordinate[1],
                'price': user['movePrice'],
                'size': user['moveSize']
            }
            scaler = MinMaxScaler()
            normalized_data = scaler.fit_transform([[item[field] for field in weights.keys()] for item in data])
            normalized_user_input = scaler.transform([[user_input[field] for field in weights.keys()]])
            for item in normalized_data:
                item[0] *= weights['x_coordinate']
                item[1] *= weights['y_coordinate']
                item[2] *= weights['price']
                item[3] *= weights['size']
            similarities = cosine_similarity(normalized_user_input, normalized_data).flatten()
            top_indices = np.argsort(similarities)[::-1][:10]
            top_houses = [data[i] for i in top_indices]
            return jsonify(top_houses)
        except Exception as e:
            return jsonify({"error": str(e)})


def change_region_coordinate(text):
    coordinateMap = {
        '강남구': (127.047059839521, 37.5179681611717),
         '서초구': (127.032683002019, 37.4836248649455),
         '강동구': (127.123686336418, 37.5300981049478),
         '강서구': (126.849532173376, 37.5509655144007),
         '강북구': (127.025449504014, 37.6391856183931),
         '관악구': (126.951501244173, 37.4782106746327),
         '광진구': (127.081909826352, 37.5385316143438),
         '구로구': (126.888292375229, 37.4955054632154),
         '금천구': (126.896036850324, 37.4570656519531),
         '노원구': (127.056268317802, 37.6545228397157),
         '동대문구': (127.039896580148, 37.5743917161622),
         '도봉구': (127.047131400119, 37.6687161285201),
         '동작구': (126.939942092863, 37.51252777344),
         '마포구': (126.901615668932, 37.5663128370109),
         '서대문구': (126.936759175119, 37.5791546257808),
         '성동구': (127.036964999975, 37.5634225092469),
         '성북구': (127.016690019544, 37.5894551333062),
         '송파구': (127.105859984389, 37.514477182474),
         '영등포구': (126.896367130558, 37.525963157053),
         '용산구': (126.990478820837, 37.5324522944579),
         '양천구': (126.866542541936, 37.5170753784215),
         '은평구': (126.928822870137, 37.6024574203071),
         '종로구': (126.978988255925, 37.5735051436739),
         '중구': (126.998009728978, 37.5641201543296),
         '중랑구': (127.09272484193, 37.6065635856848)
    }
    return coordinateMap[str(text)]

def user_info_change(user_info, want_move_region):
    return {
        "collectMoney" : int(int(str(user_info['totalAmount'])) + (int(str(user_info['annualIncome']))/12-int(str(user_info['averageMonthlyExpenditure'])))*int(str(user_info['moveDate']))),
        "moveRegion" : move_region_change(want_move_region),
        "moveHouse" : move_house_change(user_info['moveHouse']),
        "moveHouseType" : move_house_type_change(user_info['moveHouseType']),
        "moveSize" : int(str(user_info['moveSize'])),
        "movePrice" : int(str(user_info['movePrice']))
    }

def move_house_change(move_house):
    houseMap = {
        "apart": "아파트",
        "officetel" : "오피스텔"
    }
    return houseMap[move_house]

def move_house_type_change(move_house_type):
    houseTypeMap = {
        "jeonse": "전세",
        "purchaseSale": "매매",
        "monthlyRent": "월세"
    };
    return houseTypeMap[move_house_type]

def move_region_change(move_region):
    regionMap = {
        "101": "강남구",
        "102": "강동구",
        "103": "강북구",
        "104": "강서구",
        "105": "관악구",
        "106": "광진구",
        "107": "구로구",
        "108": "금천구",
        "109": "노원구",
        "110": "도봉구",
        "111": "동대문구",
        "112": "동작구",
        "113": "마포구",
        "114": "서대문구",
        "115": "서초구",
        "116": "성동구",
        "117": "성북구",
        "118": "송파구",
        "119": "양천구",
        "120": "영등포구",
        "121": "용산구",
        "122": "은평구",
        "123": "종로구",
        "124": "중구",
        "125": "중랑구",
        "201": "가평",
        "202": "고양",
        "203": "과천",
        "204": "광명",
        "205": "광주",
        "206": "구리",
        "207": "군포",
        "208": "김포",
        "209": "남양주",
        "210": "동두천",
        "211": "부천",
        "212": "성남",
        "213": "수원",
        "214": "시흥",
        "215": "안산",
        "216": "안성",
        "217": "안양",
        "218": "양주",
        "219": "양평",
        "220": "여주",
        "221": "연천",
        "222": "오산",
        "223": "용인",
        "224": "의왕",
        "225": "의정부",
        "226": "이천",
        "227": "파주",
        "228": "평택",
        "229": "포천",
        "230": "하남",
        "231": "화성",
        "30": "인천"
    }
    return regionMap[str(move_region)]