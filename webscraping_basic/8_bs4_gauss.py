import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list.nhn?titleId=103759"

res = requests.get(url)
res.raise_for_status() # 문제 있으면 프로그램 종료

soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("td",attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print("https://comic.naver.com" +link)

#만화 제목 + 링크 구하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" +cartoon.a["href"]
#     print(title,link)

#평점 구하기
total_rates = 0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.strong.get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("전체 점수 : ", total_rates / len(cartoons))