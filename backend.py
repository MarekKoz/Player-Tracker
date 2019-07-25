import sqlite3

def connect():
    connection = sqlite3.connect("Players.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Athlete (id INTEGER PRIMARY KEY, name text, team text, jersey integer, mvp integer)")
    connection.commit()
    connection.close()

connect()
    

