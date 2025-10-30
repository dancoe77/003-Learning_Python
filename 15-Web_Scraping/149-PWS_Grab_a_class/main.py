zz = "###############################################################"
print(zz)

import requests
result = requests.get('http://www.example.com')
print(type(result))
print(zz)

print(result.text)
print(zz)
import bs4

soup = bs4.BeautifulSoup(result.text, 'html.parser')
print(soup)
print(zz)

print(soup.title)
print(soup.select("title"))
print(zz)

print(soup.paragraph)
print(soup.select("p"))
print(zz)

print(soup.head)
print(soup.select("h1"))
print(zz)

print(soup.select("title")[0].text)
print(zz)

site_paragraph = soup.select("p")
print(site_paragraph)
print(zz)
print(site_paragraph[0].text)
print(zz)

url  = "https://en.wikipedia.org/wiki/Grace_Hopper"
headers = {"User-Agent": "ClassBot/0.0 (https://github.com/dancoe77/003-Learning_Python; dan@shoeman-tech.com) python-requests-3.13.9"}

res = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup)
print(zz)
print(soup.select(".vector-toc-text"))
print(zz)
print(type(soup.select(".vector-toc-text"))[1])
print(zz)
first_item = soup.select(".vector-toc-text")[1]
print(first_item)
print(zz)
print(first_item.text)
print(zz)