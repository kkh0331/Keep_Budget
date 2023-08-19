# Keep Budget
- 제 5회 KB ai Challenge 공모전 대회 참여를 목적으로 제작되었습니다.

# 프로젝트명 : 지역에 특화된 뉴스 및 매물 추천
- Main Page Capture Image<br>
<img width="480" alt="KakaoTalk_Image_2023-08-19-21-19-07" src="https://github.com/kkh0331/KB-ai/assets/99806443/5e0fa8fa-6123-4d76-b2d1-1e0f923e83bd"><br>
[시연영상을 보실려면 여기를 클릭해주세요](https://youtu.be/DEJtR_HfwHc)


# Functions
- Flask scheduler을 활용하여 매일 오전 2시마다 BeatifulSoup 모듈을 활용해서 자동으로 네이버 뉴스에서 크롤링 진행(단!! 서버가 켜져있다는 가정하에)
  - 부동산 뉴스 : 뉴스 기사에서 지역을 추출하고 감정분석(Bert 이용)을 진행하여 DB에 저장 > Donut-Chart을 활용해서 시각화 진행
  - 사건사고 뉴스 : 뉴스 기사에서 지역을 추출하고 형태소 분석(Konlpy-Twitter 이용)을 진행하여 DB에 저장 > Wort Cloud을 활용해서 시각화 진행
- 사용자가 입력한 정보를 바탕으로 추천 시스템 구현(코사인 유사도 이용)

# 프로젝트 Architecture
<img width="445" alt="스크린샷 2023-08-19 오후 9 13 10" src="https://github.com/kkh0331/KB-ai/assets/99806443/faf0a2ee-4ce6-45a4-b49e-c56c561eadb8"><br>
