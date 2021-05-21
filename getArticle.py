import requests
from bs4 import BeautifulSoup
import csv
import re


def getArticle(linksOfArticles):
    print("Phase 6: Extracting data from gathered links (estimated a minimum of 50 seconds)")
    completeData = []
    for link in linksOfArticles:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")
        try:
            time_ = soup.select_one('.caas-attr-time-style > time').contents[0]
        except:
            pass
        try:
            author = soup.select_one('.caas-attr > div').contents[0].getText()
        except AttributeError:
            author = soup.select_one('.caas-attr > div').descendants
            descendantsList = list(author)
            author = descendantsList[0]

        title = soup.select_one('.caas-title-wrapper > h1').contents[0]
        bodyToParse = soup.select_one('.caas-body')
        bodyText = ""
        for paragraphIndex, para in enumerate(bodyToParse):
            paraText = soup.select_one('.caas-body').contents[paragraphIndex].getText()
            bodyText += paraText
            bodyText += " "

        combineLabels = [time_, author, title, bodyText]
        completeData.append(combineLabels)

    print("Phase 7: All data extracted, writting to file")
    header = ["time","author","title","body text"]
    with open('dataCSV.csv', mode='w', newline='',encoding='utf-8-sig', errors='ignore') as doodler:
        doodleCursor = csv.writer(doodler)
        doodleCursor.writerow(header)
        for row in completeData:
            doodleCursor.writerow(item for item in row)

        
        

 


