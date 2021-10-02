from pygooglenews import GoogleNews
from time import sleep
from requests_html import HTMLSession
from newspaper import Article
from newspaper import Config

import requests
import json
#url = 'https://www.reuters.com/technology/sp-dow-jones-indices-launches-crypto-indices-2021-05-04/'

def get_titles(search):
    gn = GoogleNews()
    search = gn.search(search)
    articles=[]
    newsitem = search["entries"]
    i=0
    for item in newsitem:
        url=item.link
        try:
            article = Article(url)
            article.download()
            article.parse()
            news ={
                    'Headline':article.title,
                    'Article':article.text,
                    'Link':item.link,
                    "Authors":article.authors,
                    "Image":article.top_image,
                    "Date": article.publish_date
                    }
            if article.title=="Are you a robot?" or article.title=="Subscribe to read" :
                continue
            else:
                articles.append(news)
                i=i+1
                print(i,'',article.title)
                sleep(1)
        except:
            pass

    with open('news_database.json', 'w') as f:
        json.dump(articles, f)
    return

get_titles("")
