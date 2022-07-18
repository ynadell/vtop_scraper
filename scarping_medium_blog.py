from bs4 import BeautifulSoup
import requests
import re

url = "https://medium.com/@yashwanthnadella/why-care-about-climate-change-390906b8b4bd"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")
paragraphs = doc.find_all("p")
for p in paragraphs:
    print(p.text)
points = doc.find_all("li")
for li in points:
    print(li.text)
