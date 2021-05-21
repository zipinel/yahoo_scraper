import requests
from bs4 import BeautifulSoup
import csv



def homeScraper():
    linksFound = []
    res = requests.get("https://news.yahoo.com/")
    soup = BeautifulSoup(res.text, 'html.parser')

    topHero = soup.select_one('#item-0 > div a').get('href')
    articleLinkHero = "https://news.yahoo.com" + str(topHero)
    linksFound.append(articleLinkHero)

    mainCardsUnderHero = soup.select('#item-0 ul li')
    for linkIndex, link in enumerate(mainCardsUnderHero):
        partialLink = mainCardsUnderHero[linkIndex].find('a', href=True).get('href')
        FullLink = "https://news.yahoo.com" + str(partialLink)
        linksFound.append(FullLink)
    
    for articleIndex in range(1,130):
        divLocation = soup.select(f'#YDC-Stream > ul > li:nth-of-type({articleIndex}) > div > div > div > h3 > a')
        for item in divLocation:
            partialLink = item.get('href')
            articleLink = "https://news.yahoo.com" + str(partialLink)
            linksFound.append(articleLink)
    
    return linksFound




def getHome(linksOfArticles):
    completeData = []
    for link in linksOfArticles:
        res = requests.get(link, timeout=5)
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


linksOfArticles = homeScraper()
getHome(linksOfArticles)