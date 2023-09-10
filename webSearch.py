from bs4 import BeautifulSoup
import requests


#https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&ssid=59422750ead2435ab78535785c8d2c3f&sp=aff&cp=01ac0022bf&nlpv=test_dt_12&q=%E4%BD%A0%E5%A5%BD
#https://www.so.com/s?q=hello&src=srp&ssid=&fr=none&sp=aee&cp=05b0005d77&psid=fae7d2e539a00a22aa60e0c6aca219ea
#https://www.so.com/s?q=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&src=srp&ssid=&fr=none&sp=ac5&cp=082b14002a&psid=249b609a7a8ec1253c8fbd0d9a06a790

def getContent(question):
    url="https://www.so.com/s?q="+question
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
    }
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.txt,"html.parser")
    Content=soup.find()


