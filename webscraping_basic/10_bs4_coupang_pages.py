import requests
import re
from bs4 import BeautifulSoup
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status() # 문제 있으면 프로그램 종료
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    print(items[0].find("div",attrs={"class":"name"}).get_text())

    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div",attrs={"class":"name"}).get_text() # 제품 명

        # 애플 제품 제외
        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가 격

        #리퓨 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"}) # 별점
        if rate:
            rate = rate.get_text()
        else:
            continue

        rate_count = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
        if rate_count:
            rate_count = rate_count.get_text()[1:-1] # 예 (26)# 1부터 -1 까지의 것을 제외
        else:
            continue
        
        link = item.find("a",attrs = {"class":"search-product-link"})["href"]
        if float(rate) >= 4.5 and int(rate_count) >= 100:
            print(name,price,rate,rate_count)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count})개")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100)

        

