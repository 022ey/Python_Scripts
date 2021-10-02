#Description: This is a python program than can scrape and summarize news articles

#Libraries
import nltk
from newspaper import Article
import json
import datetime
import sys

#Scraping articles
url= input("Enter the url of the article that you want to summarize:")
article = Article(url)

#NLP
article.download()
article.parse()
#nltk.download('punkt')  >>>#For first time only
article.nlp()

#Get the article and it's details
article.authors
article.publish_date
article.top_image
article.summary
#print(article.text) >>> #Use this to get entire Article

#Main function
def main():
    data = {"summary": article.summary ,
            "image" : article.top_image ,
            "date" : article.publish_date ,
            "authors" : article.authors}
    #creating json dumps
    j = json.dumps(data , default = str)
    with open('data1', 'w') as f:
        f.write(j)
        f.close()
    print("********************************************")
    print("Your Requested article has been summarised")
    print("********************************************")
main()

#restart function
def restart ():
    restart = input("Press Enter to start again, or x to exit.")
    while True:
        if(restart != "x"):
            exec(open("./main.py").read())
            main()
        else:
            print ("Exiting!")
            sys.exit ((main))
restart()
