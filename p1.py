#-*- coding: cp949 -*-
import requests
from bs4 import BeautifulSoup

#�˻� Ű���� - ���̹� ����In ũ�Ѹ� �˻�
response = requests.get("https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%81%AC%EB%A1%A4%EB%A7%81")
html = response.text
soup = BeautifulSoup(html,"html.parser")

links = soup.select(".api_txt_lines.question_text")

for info in links:
    print(info.text,info.get('href'))
