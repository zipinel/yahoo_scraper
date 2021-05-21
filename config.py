
us = "https://news.yahoo.com/us/"
politics = "https://news.yahoo.com/politics/"
world = "https://news.yahoo.com/world/"
health = "https://news.yahoo.com/health/"
science = "https://news.yahoo.com/science/"
skullduggery = "https://news.yahoo.com/tagged/skullduggery/"
original = "https://news.yahoo.com/originals/"
tag360 = "https://news.yahoo.com/tagged/360/"
conspiracy = "https://news.yahoo.com/tagged/conspiracyland"



#######################################################################
##### Change politics with whatever category you want to scrape #####
categoryToUse = politics



def category():
    print("Phase 1: category " + categoryToUse + " selected")
    return categoryToUse