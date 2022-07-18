from bs4 import BeautifulSoup
import requests
import re

url = "https://medium.com/@yashwanthnadella/why-care-about-climate-change-390906b8b4bd"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")

print(doc.prettify())
