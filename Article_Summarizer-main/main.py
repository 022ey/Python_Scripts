#Description: This is a python program than can scrape and summarize news articles

#Libraries
import json
import sys

import nltk

from utils import parse_article


#Main function
def main():
    nltk.download('punkt')
    
    #Scraping articles
    url = input("Enter the url of the article that you want to summarize:")
    article = parse_article(url)

    #Get the article and it's details
    authors = article.authors
    publish_date = article.publish_date
    top_image = article.top_image
    summary = article.summary
    #print(article.text) >>> #Use this to get entire Article

    data = {"summary": summary,
            "image" : top_image,
            "date" : publish_date,
            "authors" : authors}
    #creating json dumps

    j = json.dumps(data, default=str)
    with open('data1', 'w') as f:
        f.write(j)
        f.close()

    print("********************************************")
    print("Your Requested article has been summarised")
    print("********************************************")


#restart function
def restart ():
    restart = input("Press Enter to start again, or x to exit.")
    while True:
        if restart != "x":
            exec(open("./main.py").read())
            main()
        else:
            print("Exiting!")
            sys.exit((main))


if __name__ == "__main__":
    main()
    restart()
