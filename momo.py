from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import datetime

db = sqlite3.connect('mabase.db')

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     isbn INTEGER,
     name TEXT,
     price TEXT,
     date TEXT
    
)
""")



date= datetime.datetime.now()
isbn=input("isbn ?:  ")
driver = webdriver.Chrome("C:/dev/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.momox.fr/")
driver.minimize_window()
driver.refresh()
driver.find_element_by_class_name("searchbox-input").send_keys(isbn)
time.sleep(4)
driver.find_element_by_id("buttonMediaSearchSubmit").click()
time.sleep(4)
prix = driver.find_element_by_class_name("searchresult-price").text
titre = driver.find_element_by_class_name("product-title").text
driver.quit()

print(date)
print(isbn)
print(prix)
print(titre)

cursor.execute("""INSERT INTO users( id, isbn, name, price, date) VALUES(null,?,?,?, ?)""", (isbn,titre,prix,date))
db.commit() # enregistre la base
cursor.execute("""SELECT id, isbn, name, price, date FROM users""")
rows = cursor.fetchall()
print(rows)
for row in rows:
    print('{0} : {1} - {2} - {3} -{4}'.format(row[0], row[1], row[2], row[3], row[4]))

print("fin")
db.close()