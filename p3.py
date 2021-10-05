#-*- coding: cp949 -*-
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

#입력 데이터로 네이버 뉴스 1~5 페이지 검색 후 구조체에 저장 관리 예제

class News:
    title: str = None
    link: str = None

keyword = input()

newsInfoArray =[]

for page in range(1,51,10):
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=33&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}")
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    data = soup.select(".news_tit")

    for info in data:
        newsInfo = News()
        newsInfo.title = info.text
        newsInfo.link = info.get("href")
        newsInfoArray.append(newsInfo)

for info in newsInfoArray:
    print(info.title, info.link)