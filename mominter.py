from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import datetime
from tkinter import *
import py_win_keyboard_layout

py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409) # scanner code barre ne fonctionnant qu'en UK


def prix_isbn():

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

    date = datetime.datetime.now()
    isbn = champisbn.get()


    driver = webdriver.Chrome("C:/dev/chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.get("https://www.momox.fr/")
    driver.minimize_window()
    driver.refresh()
    driver.find_element_by_class_name("searchbox-input").send_keys(isbn)
    time.sleep(4)
    driver.find_element_by_id("buttonMediaSearchSubmit").click()
    time.sleep(4)
    try:
        prix = driver.find_element_by_class_name("searchresult-price").text
    except:
        prix =str("pas de prix")
    titre = driver.find_element_by_class_name("product-title").text
    driver.quit()

    #print(date)
    #print(isbn)
    #print(prix)
    #print(titre)

    cursor.execute("""INSERT INTO users( id, isbn, name, price, date) VALUES(null,?,?,?, ?)""", (isbn, titre, prix, date))
    db.commit()  # enregistre la base
    cursor.execute("""SELECT id, isbn, name, price, date FROM users""")
    rows = cursor.fetchall()
    #print(rows)
    #for row in rows:
    #    print('{0} : {1} - {2} - {3} -{4}'.format(row[0], row[1], row[2], row[3], row[4]))

    #print("fin")
    db.close()
    lblprix['text']="Le prix est de "+str(prix)
    champisbn.focus_set()


# Interface GUI
fen = Tk()

fen.geometry("450x250")
lblnom= Label(fen,text="ISBN MOMOX")
champisbn = Entry(fen)
ok = Button(fen,text="Valider ISBN",command = prix_isbn)
lblprix = Label(fen,text ="Prix: ")
lblnom.pack()
champisbn.pack()
lblprix.pack()
ok.pack()
champisbn.focus_set()
fen.mainloop()
