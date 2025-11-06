import requests
import bs4

res = requests.get("https://quotes.toscrape.com/")
print(res.text)

soup = bs4.BeautifulSoup(res.text, "html.parser")
soup.select(".author")
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)
tags = []
for tag in soup.select(".tag-item"):
    tags.append(tag.text)
print(tags)
url = "https://quotes.toscrape.com/page/"
authors = set()
for page in range(1,11):
    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    for name in soup.select(".author"):
        authors.add(name.text)
print(authors)

page_still_valid = True
authors = set()
page = 1
while page_still_valid:
    page_url = url + str(page)
    res = requests.get(page_url)
    if "No quotes found" in res.text:
        break
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    for name in soup.select(".author"):
        authors.add(name.text)
    page = page + 1
print(authors)

