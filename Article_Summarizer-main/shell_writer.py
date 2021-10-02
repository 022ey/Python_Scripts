#Description: This is a python program than can scrape and summarize news articles

#Libraries
import nltk
from newspaper import Article

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

#print(article.text) >>> #Use this to get entire Article

#Summarize the articles
def main():
    print("******************************************")
    print("Summary:")
    print(article.summary)
    print("******************************************")
main()

#restart function
def restart ():
    restart = input("Press Enter to start again, or x to exit.")
    while True:
        if(restart != "x"):
            exec(open("./Shell_writer.py").read())
            main()
        else:
            print ("Exiting!")
            sys.exit ((main))
restart()
