"""
Read xml file
"""
from bs4 import BeautifulSoup

with open("./json_xml/xml/sample.xml", "r") as f:
    data = f.readlines()

soup = BeautifulSoup(data, "html.parser")

folders = soup.find_all("folder", string=True)
for folder in folders:
    print(folder['name'])