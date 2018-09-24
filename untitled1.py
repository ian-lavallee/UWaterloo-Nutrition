# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:21:33 2018

@author: Ian55
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print(page.status_code)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify)
print("\n children: \n")
print(list(soup.children))
print("\nType: \n")
print([type(item) for item in list(soup.children)])
print("\nhtml tag\n")
html = list(soup.children)[2]
print(html)
print("\nlist of html children\n")
print(list(html.children))
print("\n Body \n")
body = list(html.children)[3]
print(body)
print("\n body children\n")
print(list(body.children))

p = list(body.children)[1]
print(p.get_text())

soup.find_all('p')
print( "\n" + str(soup.find_all('p')))
print("\n 'p'[0] " + soup.find_all('p')[0].get_text())


