zz = "##################################################################################"
print(zz)
import requests
import bs4

url  = "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)"
headers = {"User-Agent": "ClassBot/0.0 (https://github.com/dancoe77/003-Learning_Python; dan@shoeman-tech.com) python-requests-3.13.9"}

res = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(res.text, "html.parser")
# print(soup.select(".mw-file-element"))
# print(zz)
print(soup.select(".mw-file-element")[1])
print(zz)

computer = soup.select(".mw-file-element")[1]
print(computer["src"])
print(zz)

url  = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg"
image_link = requests.get(url, headers=headers)
f = open("Deep_Blue.jpg", "wb")
f.write(image_link.content)
f.close()
