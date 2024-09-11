import LxmlSoup
import requests

html = requests.get("https://ekb.sunlight.net/catalog").text
soup = LxmlSoup.LxmlSoup(html)
links = soup.find_all("a", class_="cl-item-link js-cl-item-link js-cl-item-root-link")

for link in links:
    print(link.get("href"))
    print(link.text())
    print("-"*20)
