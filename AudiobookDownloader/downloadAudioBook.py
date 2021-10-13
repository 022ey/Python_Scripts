import requests
from bs4 import BeautifulSoup
import os


foldername = ""


def bookname2bookpage(abname):
    abname = abname.replace(" ", "+")
    # print(abname)
    searchurl = "https://audiobooklabs.com/?s=" + abname
    print(searchurl)
    searchresultpage = requests.get(searchurl)
    soup = BeautifulSoup(searchresultpage.content, "html.parser")
    # print(soup.prettify)
    resultbox = soup.find(id="primary")
    # print(resultbox)
    results = resultbox.find("h2", class_="entry-title")
    print(results)
    if results == None:
        return 0
    bookpage = results.find("a")
    bookpageurl = bookpage["href"]
    print(bookpageurl)
    return bookpageurl


def bookpage2playerpage(bookpage):
    if bookpage == 0:
        return 0
    dunnowhut = requests.get(bookpage)
    soup = BeautifulSoup(dunnowhut.content, "html.parser")
    # print(soup)
    for link in soup.find_all("a", href=True):
        if (link["href"]).split("?")[0] == "https://audiobooklabs.com/file-downloads":
            playerpage = link["href"]
            break
    return playerpage


def playerpage2fileurl(playerpage):
    global foldername
    if playerpage == 0:
        return []
    weirdbs = requests.get(playerpage)
    soup = BeautifulSoup(weirdbs.content, "html.parser")
    Name = soup.find_all("h2", {"class": "audioalbum"})
    foldername = Name[0].contents[0][:-10]
    print(f"The book being downloaded is {foldername}")
    links = []
    for link in soup.find_all("a", href=True):
        if link["href"].split(".")[-1] == "mp3":
            print(link["href"])
            links.append(link["href"])

    return links


def downloadfromfile(links):
    global foldername
    if len(links) > 0:
        try:
            print("Checking if book is already downloaded or not.")
            if not os.path.exists(foldername):
                print("Book is not downloaded.")
                print("starting to download")
                os.mkdir(foldername)
                filenum = 1
                for link in links:
                    r = requests.get(link, stream=True)
                    name = link.split("/")[-1]

                    with open(f"{foldername}/{filenum}_{name}", "wb") as mp3:
                        for chunk in r.iter_content(chunk_size=256 * 1024):
                            # writing one chunk at a time to audio file
                            if chunk:
                                mp3.write(chunk)
                    filenum = filenum + 1
                print("Successful download")
                with open(f"{foldername}/success.txt", "w") as succ:
                    succ.write("Successful Download! plox;_;")
            else:
                if os.path.exists(f"{foldername}/success.txt"):
                    print(
                        f"A successful download already exists. If you wish to redownload remove {foldername}/success.txt"
                    )
                else:
                    filenum = 1
                    for link in links:
                        r = requests.get(link, stream=True)
                        name = link.split("/")[-1]

                        with open(f"{foldername}/{filenum}_{name}", "wb") as mp3:
                            for chunk in r.iter_content(chunk_size=256 * 1024):
                                # writing one chunk at a time to audio file
                                if chunk:
                                    mp3.write(chunk)
                        filenum = filenum + 1
                    print("Successful download")
                    with open(f"{foldername}/success.txt", "w") as succ:
                        succ.write("Successful Download! plox;_;")

        except Exception as e:
            print(e)
            return e

    else:
        print("Book not found")
        return None
    return 1


def download(inputtext):
    output = downloadfromfile(
        playerpage2fileurl(bookpage2playerpage(bookname2bookpage(inputtext)))
    )
    return output


if __name__ == "__main__":
    inputtext = input("Enter book's name: ")
    download(inputtext)
