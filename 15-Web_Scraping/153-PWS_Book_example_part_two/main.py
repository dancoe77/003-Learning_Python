import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
page_num  = 1
response = requests.get(base_url.format(page_num))
print(response)
soup = bs4.BeautifulSoup(response.text, "html.parser")
products = soup.select(".product_pod")
example = products[0]
print(example.select(".star-rating.Three"))
print([] == example.select(".star-rating.Two"))
print(example.select("a")[1]["title"])
two_star_titles = []
for i in range(1,51):
    scrape_url = base_url.format(i)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)
    print(two_star_titles)
