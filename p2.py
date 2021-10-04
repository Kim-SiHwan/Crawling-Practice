#-*- coding: cp949 -*-
import requests
from bs4 import BeautifulSoup

#디시인사이드 던전앤파이터 갤러리 1~10 페이지 크롤링 연습
headers ={'User-Agent':''}
for page in range(1,11):
    
    response = requests.get("https://gall.dcinside.com/board/lists/?id=d_fighter_new2&page="+str(page),headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")

    titles = soup.select(".gall_tit.ub-word")
    writers = soup.select(".gall_writer.ub-writer")
    counts = soup.select(".gall_count")
    recommends = soup.select(".gall_recommend")
    dates = soup.select(".gall_date")

    postInfoArray =[]
    for i in range(2,len(titles)):
        tmpArray =[]
        writerInfo = writers[i].text.replace("\n"," ")
        titleInfo = titles[i].text.replace("\n"," ")
        dateInfo = dates[i].text
        countInfo = counts[i].text
        recommendInfo = recommends[i].text

        tmpArray.append(writerInfo)
        tmpArray.append(titleInfo)
        tmpArray.append(dateInfo)
        tmpArray.append(countInfo)
        tmpArray.append(recommendInfo)

        postInfoArray.append(tmpArray)

    print(postInfoArray)
