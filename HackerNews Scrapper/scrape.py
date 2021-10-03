import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get("https://news.ycombinator.com/news")
res2=requests.get("https://news.ycombinator.com/news?p=2")
soup=BeautifulSoup(res.text,'html.parser')
soup2=BeautifulSoup(res.text,'html.parser')
#print(soup.contents )
#print(soup.find(id="score_23147752"))
#print(soup.select("#score_23147752"))
links=soup.select(".storylink")
links2=soup.select(".storylink")
subtext=soup.select(".subtext")
subtext2=soup.select(".subtext")

MEGA_LINK=links+links2
MEGA_SUBTEXT=subtext+subtext2

def sorterd_by_votes(hnlist):
    a=sorted(hnlist,key=lambda k:k['votes'])
    a.reverse()
    return a
#api can be used for scrapping
def create_custom_hn(links,subtext):
    hn=[]
    for idx,lnks in enumerate(links):
        title = lnks.getText()
        href = lnks.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
           points = int(vote[0].getText().replace(' points',""))
           if points>=100:
               hn.append({'title':title,'href':href,'votes':points})
    return sorterd_by_votes(hn)

pprint.pprint(create_custom_hn(MEGA_LINK,MEGA_SUBTEXT))