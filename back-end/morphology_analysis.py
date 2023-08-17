from konlpy.tag import Twitter
import re
import string
import datetime
from news_crawling import from_crawling_to_region

jvm_path = "/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home/bin/java"
twitter = Twitter(jvmpath=jvm_path)

with open('../document/stopwords.txt', 'r') as f:
  stopwords = [word.strip() for word in f]
stopwords.append('출처')

def finalpreprocess(text):
    try:
        text = str(text)
        text = text.strip()
        text = re.compile('<.*?>').sub('', text)
        text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)
        text = re.sub('\s+', ' ', text)
        text = re.sub(r'\[[0-9]*\]',' ',text)
        text = re.sub(r'[^\w\s]', ' ', str(text).strip())
        text = re.sub(r'\d',' ',text)
        text = re.sub(r'\s+',' ',text)
        result = []
        noun_adj_tag = []
        p = twitter.pos(text)
        for word, tag in p:
            if tag in ['Noun' , 'Adjective']:
                noun_adj_tag.append(word)
        for w in noun_adj_tag:
            if len(w) > 1 and w not in stopwords:
                result.append(w)
        return " ".join(result)
    except Exception as e:
        return e

def accident_before_database(startMonth, startDay, endMonth, endDay, id1, id2):
    start_date = datetime.date(2023, startMonth, startDay)
    end_date = datetime.date(2023, endMonth, endDay)
    df = from_crawling_to_region(start_date, end_date, id1, id2)
    df['morphology'] = df['content'].apply(finalpreprocess)
    return df