from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import time as t
import json

# Returns a list of all page links in the provided site(stglink param)
def urlCatch(stglink):
    pagesList = []
    driver.get(stglink)
    pagesListElements = driver.find_elements_by_tag_name("a")
    for element in pagesListElements:
        tempPage = element.get_attribute("href")
        if isinstance(tempPage, str) and tempPage.startswith(stglink):
            pagesList.append(tempPage)
    pagesList = list(dict.fromkeys(pagesList))
    return pagesList


# Returns a list of Error messages for the provided url(stgLink parameter)
def findError(stageLink):
    errorMessageList = []
    driver.get(stageLink)
    t.sleep(2)
    logEntries = driver.get_log("browser")
    for errObject in logEntries:
        if errObject["level"] == "SEVERE" or errObject["level"] == "FATAL":
            errorMessageList.append(errObject["message"])
    return errorMessageList


# Calling the function to capture all pages in given site
websiteUrl = input("Enter webiste url :")
driver = webdriver.Chrome("./chromedriver.exe")
allPages = urlCatch("https://www.setmygoals.de/")

errorDictionery = {}

for pageLink in allPages:
    errorList = findError(
        pageLink
    )  # finderror function will capture all the Browser log error for supplied url and return a list
    errorDictionery[pageLink] = errorList
errorJson = json.dumps(errorDictionery)
print(errorJson)

f = open("logResult.json", "w")
f.write(errorJson)
f.close()
print("Results saved in file : logResult.json")
