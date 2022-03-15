import sqlite3

def connect():
    conn= sqlite3.connect("family.db")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS family (id INTEGER PRIMARY KEY, Name text, Age real, DOB integer, NickName text)")
    conn.commit()
    conn.close()

def add(Name, Age, DOB, NickName):
    conn= sqlite3.connect("family.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO family VALUES (NULL, ?, ?, ?, ?)",(Name, Age, DOB, NickName))
    conn.commit()
    conn.close()

def show():
    conn= sqlite3.connect("family.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM family")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Name= "", Age= "", DOB="", NickName=""):
    conn= sqlite3.connect("family.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM family WHERE Name= ? OR Age= ? OR DOB= ? OR NickName= ?",(Name, Age, DOB, NickName))
    rows= cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn= sqlite3.connect("family.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM family WHERE id= ?",(id,))
    conn.commit()
    conn.close()

def update(id, Name, Age, DOB, NickName):
    conn= sqlite3.connect("family.db")
    cur= conn.cursor()
    cur.execute("UPDATE family SET Name= ?, Age= ?, DOB= ?, NickName= ? WHERE id=?",(Name, Age, DOB, NickName, id))
    conn.commit()
    conn.close()


connect()
#add("Rajendra Gyawali", 32, 2046, "Dai")
#delete(1)
#update(2, "rabin", 18, 2059, "dai")
#print(show())
#print(search(DOB=2059)) 