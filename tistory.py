import feedparser, datetime

tistory_uri="https://hr1588.tistory.com/" #Your blog address here
feed = feedparser.parse(tistory_uri+"/rss")

markdown_text = """
### 안녕하세요 :)

### Interest   
     - python, no-code-ml을 활용한 Data Anlaysis
     - ML/DL을 활용한 타겟 분석
     - Natural Language Processing

### github stats  

<div id="main" align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=hr1588&count_private=true&show_icons=true&theme=radical"
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
<!--         <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=hr1588&layout=compact"   
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>  -->
</div>

### About Me  
<p align="center">
    <a href="https://hr1588.tistory.com/"><img src="https://img.shields.io/badge/Blog-FF5722?style=flat-square&logo=Blogger&logoColor=white"/></a>
    <a href="mailto:gaiqclass@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=gaiqclass@gmail.com"/></a>
</p>

### Tech
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Anaconda-44A833?style=flat&logo=Anaconda&logoColor=white"/>
<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Postgresql-4169E1?style=flat&logo=Postgresql&logoColor=white"/>

### 📕 Latest Blog Posts   

""" # list of blog posts will be appended here

lst = []

for i in feed['entries'][:1]:
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
