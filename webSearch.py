from bs4 import BeautifulSoup
import requests


def get_name(self):
    return "webSearch"
def run(self,data):
    #功能代码
    return
    
def getContent(question):
    url="https://www.so.com/s?q="+question
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
    }
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.txt,"html.parser")
    Content=soup.find()


