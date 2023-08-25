# Keep Budget
- 제 5회 KB ai Challenge 공모전 대회 참여를 목적으로 제작되었음
- 비록 본선진출에는 실패했지만, 금융 관련 공모전을 경험해 볼 수 있는 시간이었음

# 내 집 마련을 위한 로드맵, Keep Budget이 도와드립니다
- 이사하려고 하는 지역의 상황 및 매물을 파악하기 위한 목적으로 만들어짐
- Main Page Capture Image<br>
<img width="500" alt="스크린샷 2023-08-25 오후 9 48 58" src="https://github.com/kkh0331/Keep_Budget/assets/99806443/73de606f-7406-4d25-9b52-c1f55a07bc3b"><br>
[시연영상을 보실려면 여기를 클릭해주세요](https://youtu.be/DEJtR_HfwHc)


# Functions
- Flask scheduler을 활용하여 매일 오전 2시마다 BeatifulSoup 모듈을 활용해서 자동으로 네이버 뉴스에서 크롤링 진행(단!! 서버가 켜져있다는 가정하에)
  - 부동산 뉴스 : 뉴스 기사에서 지역을 추출하고 감정분석(Bert 이용)을 진행하여 DB에 저장 > Donut-Chart을 활용해서 시각화 진행
  - 사건사고 뉴스 : 뉴스 기사에서 지역을 추출하고 형태소 분석(Konlpy-Twitter 이용)을 진행하여 DB에 저장 > Word Cloud을 활용해서 시각화 진행
- 사용자가 입력한 정보를 바탕으로 추천 시스템 구현(코사인 유사도 이용)

# 프로젝트 Architecture
<img width="500" alt="스크린샷 2023-08-25 오후 9 50 37" src="https://github.com/kkh0331/Keep_Budget/assets/99806443/0c4a9ee5-48fa-429e-988d-08ca354708eb"><br>
