import sqlite3

def connect():
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Athlete (id INTEGER PRIMARY KEY, name text, team text, jersey integer, mvp integer)")
    connection.commit()
    connection.close()

def insert(name, team, jersey, mvp):
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Athlete VALUES (NULL, ?, ?, ?, ?)", (name, team, jersey, mvp))
    connection.commit()
    connection.close()

def update(id, name, team, jersey, mvp):
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Athlete SET name=?, team=?, jersey=?, mvp=? WHERE id=?", (name, team, jersey, mvp, id))
    connection.commit()
    connection.close()  

def delete(id):
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Athlete WHERE id=?", (id,))
    connection.commit()
    connection.close()  

def search(name = "", team = "", jersey = "", mvp = ""):
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Athlete WHERE name=? OR team=? OR jersey=? OR mvp=?", (name, team, jersey, mvp))
    data = cursor.fetchall()
    connection.close()
    return data

def view():
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Athlete")
    data = cursor.fetchall()
    connection.close()
    return data

connect()
