from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import datetime
from tkinter import *
import py_win_keyboard_layout
# print(py_win_keyboard_layout.get_foreground_window_keyboard_layout())
py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)  # scanner code barre ne fonctionnant qu'en UK
py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x08090809)

def history():
    #py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x040C040C)
    histo = sqlite3.connect('mabase.db')


    try:

        cursor = histo.cursor()
        isbn2 = (int(champisbn.get()),)
        # print (isbn2)
        # cursor.execute("SELECT id, isbn, name, price, date FROM users WHERE isbn = ? ORDER BY date DESC", isbn2)
        cursor.execute("SELECT *, oid date FROM users WHERE isbn = ? ORDER BY date DESC", isbn2)
        rows = cursor.fetchmany(10)
        hh = ''

        for row in rows:
            # hh = ('{0} : {1} - {2} - {3} -{4}'.format(row[0], row[4], row[1], row[2], row[3]))
            hh += str(row[4]) + "  ---->  " + str(row[3]) + "\n"
            lblhisto = Label(fen, text=hh)
            lblhisto.grid(row=8, column=0, columnspan=2)




    except:
        lblhisto = Label(fen, text="Pas d'historique manque ISBN")
        lblhisto.grid(row=8, column=0, columnspan=2)

    histo.close()




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
        prix = str(" => Pas de prix")
    titre = driver.find_element_by_class_name("product-title").text
    driver.quit()

    # print(date)
    # print(isbn)
    # print(prix)
    # print(titre)

    cursor.execute("""INSERT INTO users( id, isbn, name, price, date) VALUES(null,?,?,?, ?)""",
                   (isbn, titre, prix, date))
    db.commit()  # enregistre la base
    cursor.execute("""SELECT id, isbn, name, price, date FROM users""")
    # rows = cursor.fetchall()
    # print(rows)
    # for row in rows:
    #    print('{0} : {1} - {2} - {3} -{4}'.format(row[0], row[1], row[2], row[3], row[4]))

    # print("fin")
    db.close()
    lblprix['text'] = "Le prix est de " + str(prix)
    champisbn.focus_set()


# Interface GUI
fen = Tk()
fen.title('MOMOX PRICE')
fen.geometry("300x400")
lblnom = Label(fen, text="ISBN MOMOX")
champisbn = Entry(fen)
ok = Button(fen, text="Valider ISBN", command=prix_isbn)
histok = Button(fen, text="Historique", command=history)
lblprix = Label(fen, text="Prix: ")
lblnom.grid(row=1,column=0,padx=10)
champisbn.grid(row=2,column=0,padx=10)
lblprix.grid(row=3,column=0,padx=10)
ok.grid(row=4,column=0,padx=10,pady=10,ipadx=96)
histok.grid(row=5,column=0,padx=10,pady=10,ipadx=100)

champisbn.focus_set()

fen.mainloop()
py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x040C040C)