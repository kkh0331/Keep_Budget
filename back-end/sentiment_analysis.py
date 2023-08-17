import tensorflow as tf
from nltk import sent_tokenize
from transformers import TFBertForSequenceClassification, BertTokenizer
import numpy as np
import datetime
import tensorflow_addons as tfa
import ssl
from news_crawling import from_crawling_to_region

# SSL 검증 비 활성화(보안에 문제는 있음) but nltk.download을 위해서 임시로 허용
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk
nltk.download('punkt')

# 모델 경로 database 폴더 안에서 사용할 수 있도록 변경했음...

BEST_MODEL_NAME = './model/best_model.h5'

sentiment_model_best = tf.keras.models.load_model(BEST_MODEL_NAME, custom_objects={'TFBertForSequenceClassification': TFBertForSequenceClassification})

MODEL_NAME = "klue/bert-base"
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

MAX_SEQ_LEN = 64

def convert_data(X_data):
    tokens, masks, segments, targets = [], [], [], []
    for X in X_data:
        token = tokenizer.encode(X, truncation = True, padding = 'max_length', max_length = MAX_SEQ_LEN)
        num_zeros = token.count(0)
        mask = [1] * (MAX_SEQ_LEN - num_zeros) + [0] * num_zeros
        segment = [0]*MAX_SEQ_LEN
        tokens.append(token)
        masks.append(mask)
        segments.append(segment)
    tokens = np.array(tokens)
    masks = np.array(masks)
    segments = np.array(segments)
    return [tokens, masks, segments]

# 중립 0, 긍정 1 , 부정 2
def major_sentiment_to_text(major):
  if major == 0:
    return "중립"
  elif major == 1:
    return "긍정"
  else:
    return "부정"

def text_to_result(text):
    text = str(text)
    sentence_tokens = sent_tokenize(text)
    input = convert_data(sentence_tokens)
    predicted_value = sentiment_model_best.predict(input) # 예측하기
    predicted_label = np.argmax(predicted_value, axis=1) # 예측된 라벨(각 문장별로 예측 결과)
    major_sentiment = np.bincount(predicted_label).argmax() # 예측된 라벨 중 가장 많은 라벨(최빈값)
    result_list = [0, 0, 0]
    for index in predicted_label:
        result_list[int(index)] += 1
    return {"중립":round(result_list[0]/sum(result_list),2), "긍정" : round(result_list[1]/sum(result_list),2), "부정" : round(result_list[2]/sum(result_list),2), "최종" : major_sentiment_to_text(major_sentiment)}

def final_before_database(startMonth, startDay, endMonth, endDay, id1, id2):
    start_date = datetime.date(2023, startMonth, startDay)
    end_date = datetime.date(2023, endMonth, endDay)
    df = from_crawling_to_region(start_date, end_date, id1, id2)
    for index, row in df.iterrows():
        result = text_to_result(row['content'])
        for resKey, resValue in result.items():
            df.at[index, resKey] = resValue
    return df