import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
page_num  = 1
response = requests.get(base_url.format(page_num))
print(response)
soup = bs4.BeautifulSoup(response.text, "html.parser")
class_res = soup.select(".product_pod")
print(class_res)