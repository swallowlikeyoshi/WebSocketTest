import sqlite3
from datetime import datetime

DB_path = 'chatting_DB.db'
connection = sqlite3.connect(DB_path)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS texts (date DATETIME, user_name text, chat text)")
cur.execute("CREATE TABLE IF NOT EXISTS users (date DATETIME, user_name text, is_online BIT)")

def texts(session_info, texts):
    DB_path = 'chatting_DB.db'
    connection = sqlite3.connect(DB_path)
    cur = connection.cursor()
    values = (datetime.now(), session_info['name'], texts)
    cur.execute("INSERT INTO texts VALUES (?, ?, ?)", values)
    connection.commit()
    connection.close()
    return

def users(session_info, isOnline):
    return