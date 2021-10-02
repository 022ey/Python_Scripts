import requests
from bs4 import BeautifulSoup

def zee():
    url = 'https://zeenews.india.com/technology'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    cl = soup.findAll(class_='sec-con-box')
    count=0
    s = ""

    for i in cl:
        count = count + 1
        if count == 15:
            break
        x=i.text.find("\n\n\n")
        s = s + "\n🌐" + i.text[3:x]
        
    return s
  print(zee())
