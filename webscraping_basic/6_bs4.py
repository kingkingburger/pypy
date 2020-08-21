import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status() # 문제 있으면 프로그램 종료

soup = BeautifulSoup(res.text,  "lxml") #우리가 가져온 res.text를 lxml을 이용해서 객체로 만든것이다.
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a 엘리먼트 출력
# print(soup.a.attrs) # a 엘리먼트의 속성정보 출력
#print(soup.a["href"]) # a["속성값"] 속성 값 정보를 출력할 수 있다.

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# # class 값이 Nbtn_upload인 값인 a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"}))
# # class 값이 Nbtn_upload인 값인 element를 찾아줘

# #print(soup.find("li", attrs={"class":"rank01"}))
#rank1 = soup.find("li", attrs={"class":"rank01"})
# # #print(rank1.a.get_text())
# # rank2 = rank1.next_sibling.next_sibling
# # rank3 = rank2.next_sibling.next_sibling
# # rank2 = rank3.previous_sibling.previous_sibling
# # print(rank2.a.get_text())
# # print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")

#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="여신강림-118화")
print(webtoon)