from bs4 import BeautifulSoup
import requests
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text , "lxml")

items = soup.find("tbody").find_all("tr")

for idx, item in enumerate(items):
    col = item.find_all("td")
    # a_item = item.find("td",attrs={"class":"col1"}).find("div",attrs={"class":"txt_ac"}).get_text()
    # b_item = item.find("td",attrs={"class":"col2"}).find("div",attrs={"class":"txt_ac"}).get_text()
    # c_item = item.find("td",attrs={"class":"col3"}).find("div",attrs={"class":"txt_ac"}).get_text()
    # d_item = item.find("td",attrs={"class":"col4"}).find("div",attrs={"class":"txt_ac"}).get_text()
    # e_item = item.find("td",attrs={"class":"col5"}).find("div",attrs={"class":"txt_ac"}).get_text()
    print("============= 매물{} ==========".format(idx))
    # print("거래 : ", a_item) 
    # print("면적 : ", b_item)        
    # print("가격 : ", c_item)        
    # print("동 : ", d_item)        
    # print("층 : ", e_item)  
    print("거래 : ", col[0].get_text().strip()) 
    print("면적 : ", col[1].get_text().strip() , "(공급/전용)")        
    print("가격 : ", col[2].get_text().strip() , "(만원)")        
    print("동 : ", col[3].get_text().strip())        
    print("층 : ", col[4].get_text().strip()) 

      
