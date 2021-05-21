from bs4 import BeautifulSoup
import time
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def seleniumAction(source):
    print("Phase 2: Selenium scroll down started (estimated a minimum of 30 seconds)")
    cwd = os.getcwd()
    pathToChromeDriver = os.path.join(cwd, "resources\chromedriver.exe")
    driver = webdriver.Chrome(executable_path=pathToChromeDriver)
    driver.get(source)
    driver.maximize_window()
    driver.find_element_by_name("agree").click()
    driver.get(source)
    for stretch in range(1,40):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    time.sleep(3)
    stretchedPage = driver.page_source
    driver.close()
    print("Phase 3: Selenium scroll down completed successfully")
    print("Phase 4: Starting to gather all links from category")
    return stretchedPage


def categoryScraper(category):
    stretchedPage = seleniumAction(category)
    soup = BeautifulSoup(stretchedPage, features="html.parser")
    linksFound = []
    for articleIndex in range(1,130):
        divLocation = soup.select(f'#YDC-Stream > ul > li:nth-of-type({articleIndex}) > div > div > div > h3 > a')
        for item in divLocation:
            partialLink = item.get('href')
            articleLink = "https://news.yahoo.com" + str(partialLink)
            adRemover = "beap.gemini.yahoo.com"
            if adRemover not in articleLink:
                linksFound.append(articleLink)
    return linksFound

