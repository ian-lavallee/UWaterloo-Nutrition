# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 21:56:15 2018

@author: Ian55
"""
import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('Food.db')


c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE foods
#             (Title, Calories, Fat, Carbs, Protein)''')

# Insert a row of data
c.execute("INSERT INTO foods VALUES ('Cream Cheese', 21 ,23,24,35.14)")
c.execute("INSERT INTO foods VALUES ('Cat', 35, 33, 33, 33)")


c.execute("DELETE FROM foods")
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

for i in range(0, 5000):
    print(i)
    page = requests.get("https://uwaterloo.ca/food-services/menu/product/" + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')

    foodtitle = soup.find(class_='uw-site--title')
    title = list(foodtitle.children)[1]
    if title.contents[0] == 'Page not found':
        continue
    uwtitle = title.get_text()[21:]
    print(uwtitle)
    dl_data = soup.find_all("dd")
    for d in dl_data:
        print(d.string)
    #nutrition = soup.find(class_='nutrients')
    #for n in nutrition:
    #    print(n.span.string)
    #th = soup.find_all('th')
    #print(list(th)[6])


    table = soup.find('table')
    #rows = list()
    #for row in table.findAll('tr'):
    #    rows.append(row)
    #print(rows[4].string)
    #for row in rows:
    #    print("This row is " + str(row.span) + " and its value is " + str(row.string))
    nutrients = soup.find(class_="nutrients")
    nutrients = list(nutrients)
    for n in nutrients:
        if n.contents[1].span is not None:
            print(n.contents[0].span.string + " : " + str(n.contents[0].contents[1])
                  + " The percent value is: " + str(n.contents[1].span.string) + "%")
        else:
            print(n.contents[0].span.string + " : " + str(n.contents[0].contents[1]))

    Calories = "N/A"
    Fat = "N/A"
    Carbs = "N/A"

    for nutrient in nutrients:
        if nutrient.contents[0].span.string == "Calories":
            Calories = str.strip(nutrient.contents[0].contents[1])
        if nutrient.contents[0].span.string == "Fat":
            Fat = str.strip(nutrient.contents[0].contents[1])
        if nutrient.contents[0].span.string == "Carbohydrate":
            Carbs = str.strip(nutrient.contents[0].contents[1])
        if nutrient.contents[0].span.string == "Protein":
            Protein = str.strip(nutrient.contents[0].contents[1])

    print(Calories)
    print(Fat)
    print(Carbs)
    print(Protein)

    c.execute("INSERT INTO foods VALUES (?, ?, ?, ?, ?)", (uwtitle, Calories, Fat, Carbs, Protein))
    conn.commit()

    # In future maybe add minerals/micronutrients, for now I only care about macros

    minerals = soup.find(class_="minerals")
    if minerals is None:
        continue
    minerals = list(minerals)
    for m in minerals:
        print(m.span.string + " " + str(m.contents[1].span.string))
    #percent = table.find_all('td')
    #table = table.find_all('th')
    #for i in range(2, len(percent), 1):
    #    if percent[i].span is not None:
    #        print("Percentage is %" + percent[i].span.string)
    #print(table[4].contents)


    #print(str(table[4].contents[0].string) + " : " + str(table[4].contents[1]))


    #serving = soup.find(class_="serving_size")
    #print(serving.contents[0].string)



   # rows = soup.find_all('tr')
   # for tr in rows:
    #    print(tr)

