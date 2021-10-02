import requests
import pyttsx3
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track
from rich.progress import Progress
from time import sleep
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich import box
import sys
import random
import pyfiglet

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    try:

        engine.say(audio)
        engine.runAndWait()
    except KeyboardInterrupt:
        quit()
        exit(0)    


console=Console()
console.rule("[bold red]Python Quote Generator")

result = pyfiglet.figlet_format("Welcome To Python Quote Tool", font = "small" )
print(result)

with Progress() as progress:

    task1 = progress.add_task("[bold cyan]Fetching Beautiful Quote for You.....", total=100)
    while not progress.finished:
        progress.update(task1, advance=0.5)
        sleep(0.02)

def getQuote(pg,count):
    try:
        
        page = requests.get(
                "https://www.goodreads.com/quotes?page="+str(pg))
        soup = BeautifulSoup(page.content, 'html.parser')
        quote = soup.find_all(class_='quote')
        cnt=1;

        for q in quote:
                    if(cnt>count):
                        break
                    quote_text=q.find('div',class_='quoteText')
                    authors=q.find('span',class_='authorOrTitle')
                    quote=quote_text.text
                    author=authors.text
                    author=author.split(' " ',1)[0]
                    if(len(quote)>400):
                        continue
                    print(Panel.fit("[bold yellow]"+quote))
                    
                    speak(quote)
                    
                    cnt+=1
    except (KeyboardInterrupt, SystemExit):
        print("Thanks")
        sys.exit()
        



def main():
    speak("Welcome to Python Quote Generator tool ! Thanks for using this tool.")
    while True:
        try:
            count=int(console.input("[bold red]How many quotes you want to listen?Please Enter  "))
            if count <=0:
                print('Please Enter Number Greater Than 0')
                continue
            break
        except:
            print("[bold red]Give me Only Number Please")
            
        
    pg=random.randint(1,5)
    getQuote(pg,count)
    op=''

    while op!="N":
        print("[bold cyan]More Quote ? Y/N")
        op=input()
        if(op.upper()=="Y"):
                try:
                    count=int(console.input("[bold red]How many quotes you want to listen?Please Enter  "))
                    if count <=0:
                        print('Please Enter Number Greater Than 0')
                        continue
                    break
                except:
                    print("[bold red]Give me Only Number Please")
                pg+=1
            
                getQuote(pg,count)

        else:
            break
    tk=("Thanks for using Python Quote Generator tool. If You Like this tool please Give star on https://github.com/kRavi07/python-quote-cli ")
    print(Panel("[bold green]"+tk))
    speak(tk)
    print("[bold yellow]This tool is Created By Ravi Kant Kumar ")
    speak("This tool is Created By Ravi Kant Kumar ")     
    
    

main()

