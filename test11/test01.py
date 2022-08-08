# file: test01.py

import requests as req
from bs4 import BeautifulSoup as bs

url = 'http://192.168.56.1/www/'
resp = req.get(url)
print(resp.text)