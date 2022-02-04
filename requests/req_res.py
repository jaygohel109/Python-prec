"""
get, post, put, auth, delays, etc.
"""

import requests

print("GET!!")
payload1 = { 'page': 2, 'count': 10}
#r = requests.get("https://httpbin.org/get", params= payload1)
#print(r.text)
#print(r.url)

print("POST!!")
payload2 = {'username': 'honey', 'password': 'testing'}
#r = requests.post("https://httpbin.org/post", data= payload2)
#print(r.text)
'''But its mostly used as json so,'''
#print(r.json())

print("AUTH!!")
#r = requests.get("https://httpbin.org/basic-auth/honey/testing", auth= ('honey', 'testing'))
#print(r.text)

print("If wrong credentials")
#r = requests.get("https://httpbin.org/basic-auth/honey/testing", auth= ('honeyp', 'testing'))
#print(r)

print("Delays!!")
print("When delay < timeout")
#r = requests.get("https://httpbin.org/delay/2", timeout=3)
#print(r)

print("When delay > timeout")
r = requests.get("https://httpbin.org/delay/5", timeout=3)
print(r)

