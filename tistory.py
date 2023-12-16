# import feedparser, datetime
# from urllib.parse import quote

# tistory_uri="https://hr1588.tistory.com/" #Your blog address here
# feed = feedparser.parse(tistory_uri+"/rss")

# markdown_text = """
# ## 안녕하세요 :)

# ## Interest   
#      - python, KNIME를 활용한 Data Anlaysis
#      - ML/DL을 활용한 소비자 분석
#      - Natural Language Processing

# ## github stats  

# <div id="main" align="center">
#     <img src="https://github-readme-stats.vercel.app/api?username=hr1588&count_private=true&show_icons=true&theme=radical"
#         style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
# <!--         <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=hr1588&layout=compact"   
#         style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>  -->
# </div>

# ## About Me  
# <p align="center">
#     <a href="https://hr1588.tistory.com/"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=Blogger&logoColor=white"/></a>
#     <a href="mailto:gaiqclass@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=gaiqclass@gmail.com"/></a>
# </p>

# ## Tech
# <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
# <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/>
# <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
# <img src="https://img.shields.io/badge/Postgresql-4169E1?style=flat-square&logo=Postgresql&logoColor=white"/>
# <img src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=R&logoColor=white"/>

# ## Certification
# - KNIME L1 (2023.11.24)
# - SQLD (2023.10.06)
# - 빅데이터 분석기사 (2023.07.14) 
# - ADsP (2022.09.23)
# - 컴퓨터 활용능력 1급 (2022.03.11)

# ### 📕 Latest Blog Posts   

# """ # list of blog posts will be appended here

# lst = []

# for i in feed['entries'][:1]:
#     markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"
#     print(i['link'], i['title']) 

# f = open("README.md",mode="w", encoding="utf-8")
# f.write(markdown_text)
# f.close()

# ## Projects

# ### 연구학점 I - 금융 데이터 선행연구 분석 (2022.03.09 ~ 2022.05.25)
# - "<a href='https://hr1588.tistory.com/category/주식%20선행연구%20분석'>블로깅</a>"
# - "<a href='https://github.com/hr1588/Lab_study/tree/main/kospi_project'>깃허브</a>"
#      - "코스피 방향 예측을 위한 하이브리드 머신러닝 모델: 선행연구 분석
#      - 개발 언어 : KNIME, Python
#      - 주식 도메인 및 ML 알고리즘, 시계열 분석 정리
#      - KNIME과 Python으로 선행연구 방법론 구현

# ### 제1회 KRX 금융 빅데이터 활용 아이디어 경진대회 (2022.06.27 ~ 2022.07.29)
# - [코드 공유](https://dacon.io/codeshare/5528)
# - [블로깅](https://hr1588.tistory.com/29)
#     - 개인 투자자의 분산 투자를 위한 정보 제공 플랫폼 "크로와상" 기획
#     - 개발 언어 : Python
#     - 사용 데이터 : 네이버 금융 뉴스, 2021년 1분기 주식 일별 시세정보
#     - 수익률과 샤프지수를 기반으로 한 상관 지표, 기사 내 단어 빈도 분석 기반 점수 지표 제공
#     - 74팀 중 예선 7등으로 마무리
