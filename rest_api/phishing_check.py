"""
Python program to check whether given url is safe or not
"""


import requests
import base64
import json
import urllib3

# headers = {
#     'format': 'json',
# }

# def get_url_with_ip(URI):
#     """Returns url with added URI for request"""
#     url = "http://checkurl.phishtank.com/checkurl/"
#     new_check_bytes = URI.encode()
#     base64_bytes = base64.b64encode(new_check_bytes)
#     base64_new_check = base64_bytes.decode('ascii')
#     url += base64_new_check
#     return url

# def send_the_request_to_phish_tank(url, headers):
#     """This function sends a request."""
#     response = requests.request("POST", url=url, headers=headers)
#     return response

# new_check = 'https://atsdddatffsd.weebly.com/'

# url = get_url_with_ip(new_check)
# r = send_the_request_to_phish_tank(url, headers)

endpoint = "https://checkurl.phishtank.com/checkurl/"
url = "http://www.travelswitchfly.com/"
# r = requests.post(endpoint, data={"url": url, "format": "json"})
# dict = r.json()

# if dict['results']['in_database'] == True:
#     print("Its in a database!")
#     if dict['results']['verified'] == True:
#         print("Oh no its a phish!!")
#     else:
#         print("Good to go")
# else:
#     print("I haven't met this url in my whole")

http = urllib3.PoolManager()

res = http.request('POST', url= endpoint, body=url)
print(res)