import config
import getArticle
import categoryScraper



data = config.category()
linksOfArticles = categoryScraper.categoryScraper(data)
print("Phase 5: All links gathered")
getArticle.getArticle(linksOfArticles)

print("Scrape Complete !")

