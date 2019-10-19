data = open("books.csv", encoding="utf8")

#convert each row in book.csv into tuple. data_list is a list of all those tuples
data_list = []
for i in data.readlines():
    q = []
    index1 = i.index(",")
    index2 = i.index(",", index1+1)
    index3 = i.index(",", index2+1)
    a = i[:index1]
    b = i[(index1+1):index2]
    c = i[(index2+1):index3]
    d = i[(index3+1):-2]
    q.append(a)
    q.append(b)
    q.append(c)
    q.append(d)
    q_t = tuple(q)
    data_list.append(q_t)
data_list = data_list[1:]

import sqlite3

def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY, Title varchar, Author varchar, Rating float, ISBN varchar)") #for identity column in SQLite, 'INTEGER PRIMARY KEY' has to be added after the column name in order to for values in the column to be generated automatically
    conn.commit()
    conn.close()

connect()

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    alldata = cur.fetchall()  # return a list of tuples
    conn.commit()
    conn.close()
    return alldata

def insert(title, author, rating, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)",(title, author, rating, isbn)) #for SQLite, specify NULL for identity column -> the column will generate value automatically
    conn.commit()
    conn.close()

# populate all data from books.csv to books.db
"""
for i in data_list:
    insert(i[0], i[1], float(i[2]), i[3])
"""

def search(title = '', author = '', rating = '', isbn = ''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR rating = ? OR isbn = ?",(title, author, rating, isbn))
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE ID = ?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, rating, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET Title = ?, Author = ?, Rating = ?, ISBN = ? WHERE ID = ?",(title, author, rating, isbn, id))
    conn.commit()
    conn.close()

connect()

#print(view()[2:7])
