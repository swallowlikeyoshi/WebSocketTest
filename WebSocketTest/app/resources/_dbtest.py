import sqlite3


conn = sqlite3.connect('chatting_DB.db')
cur = conn.cursor()
cur.execute('SELECT * FROM logs')

print('--------------logs----------------')
for i in cur.fetchall():
    print(i[0], i[2], i[3], i[4])
print('----------------------------------')