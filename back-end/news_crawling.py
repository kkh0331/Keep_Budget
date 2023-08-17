# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def news_crawling(start_date, end_date, id1, id2):
    # 네이버 경제 부동산 뉴스 > id1 = 101(경제), id2 = 260(부동산)
    base_url = f"https://news.naver.com/main/list.naver?mode=LS2D&mid=sec&sid1={id1}&sid2={id2}&date="
    headers = {'User-Agent': 'Mozilla/5.0'}

    news_data = []
    prev_news_list = None

    # 날짜 범위를 설정하여 크롤링
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y%m%d')
        page = 1
        while True:
            # 날짜별 페이지 수 조절
            # if page == 3:
            #     break
            sub_url = f"{base_url}{date_str}&page={page}"
            response = requests.get(sub_url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 뉴스 리스트에서 기사 정보 추출
                news_list = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li')
                if not news_list:
                    break
                if prev_news_list == news_list:
                    break
                prev_news_list = news_list

                for news in news_list:
                    try:
                        title = news.select_one('dl > dt:nth-child(2) > a').text.strip()
                        url = news.select_one('dl > dt:nth-child(2) > a')['href']
                        img_url = news.select_one('dl > dt.photo > a > img')['src']
                        summary = news.select_one('dl > dd > span.lede').text.strip()
                        # 기사 본문 링크를 따라가서 본문 가져오기
                        article_response = requests.get(url, headers=headers)
                        if article_response.status_code == 200:
                            article_soup = BeautifulSoup(article_response.text, 'html.parser')
                            content = article_soup.select_one('#dic_area').text.strip().replace('\u200b', '').replace('\xa0', '').replace('\r', '').replace('\n', '').replace('\t', '')
                            date = article_soup.select_one('#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span').text.strip()
                        else:
                            content = ''
                            date = ''

                        news_data.append({'date': date,
                                        'title': title,
                                        'url': url,
                                        'img_url': img_url,
                                        'summary': summary,
                                        'content': content
                                        })
                    except:
                        continue
            else:
                break
            page += 1
        current_date += datetime.timedelta(days=1)
    return pd.DataFrame(news_data)

region_list = ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구", "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구", "인천", "수원", "고양", "성남", "부천", "화성", "안산", "남양주", "안양", "평택", "시흥", "파주", "의정부", "김포", "광주", "광명", "군포", "하남", "오산", "양주", "이천", "구리", "안성", "포천", "의왕", "양평", "여주", "동두천", "가평", "과천", "연천", "용인"]

# 겹치는 지역 없애기
def is_region(text, region):
    if region == "중구":
        if text.find("대구") != -1 or text.find("인천") != -1:
            return 0
    if text.find(region) != -1:
        return 1
    else:
        return 0

def df_extend_region(df):
    for region in region_list:
        df[region] = df['content'].apply(lambda content: is_region(content, region))

def from_crawling_to_region(start_date, end_date, id1, id2):
    df = news_crawling(start_date, end_date, id1, id2)
    df = df[df['content'] != '']
    df_extend_region(df)
    return df
