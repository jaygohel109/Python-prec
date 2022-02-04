"""
Basics of requests library and a get request
"""
import requests

r = requests.get("https://xkcd.com/353/")
r_img = requests.get("https://imgs.xkcd.com/comics/python.png")

"""Basics for text/html"""
# print(r)
# print(dir(r))
# print(r.text)
# print(r.status_code)

"For byte/image"
with open('./requests/comic.png', "wb") as f:
    f.write(r_img.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)
