import requests
from bs4 import BeautifulSoup
import csv
import re


def coronavirusScrape():
    linksFound = []
    res = requests.get("https://news.yahoo.com/coronavirus")
    soup = BeautifulSoup(res.text, 'html.parser')

    mainEventsLeftSide = soup.select_one('.events')
    for link in mainEventsLeftSide.find_all('a'):
        linksFound.append(link.get('href'))

    topHero = soup.select_one('#top-stories-hero div:first-child')
    descendantsList = list(topHero.descendants)
    link = descendantsList[0].find('a', href=True).get('href')
    articleLinkHero = "https://news.yahoo.com" + str(link)
    linksFound.append(articleLinkHero)

    mainCardsUnderHero = soup.select('.simple-list-item')
    for linkIndex, link in enumerate(mainCardsUnderHero):
        partialLink = mainCardsUnderHero[linkIndex].find('a', href=True).get('href')
        FullLink = "https://news.yahoo.com" + str(partialLink)
        linksFound.append(FullLink)
 
    mainVideoBottom = soup.select_one('#lead-item-meta')
    link = mainVideoBottom.find('a', href=True).get('href')
    articleLinkVideo = "https://news.yahoo.com" + str(link)
    linksFound.append(articleLinkVideo)


    return linksFound





def getCorona(linksOfArticles):
    completeData = []
    for link in linksOfArticles:
        res = requests.get(link)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            try:
                time = soup.select_one('.caas-attr-time-style > time').contents[0]
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
        else:
            print(link + "  <---   404 link broken   -------------")
        combineLabels = [time, author, title, bodyText]
        completeData.append(combineLabels)

    print("Scrape completed !")
    header = ["time","author","title","body text"]
    with open('dataCSV.csv', mode='w', newline='',encoding='utf-8-sig', errors='ignore') as doodler:
        doodleCursor = csv.writer(doodler)
        doodleCursor.writerow(header)
        for row in completeData:
            doodleCursor.writerow(item for item in row)


linksOfArticles = coronavirusScrape()
getCorona(linksOfArticles)
