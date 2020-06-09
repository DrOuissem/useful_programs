import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute(''' UPDATE Students set AGE = 23 WHERE Id = 2233
''')


conn.commit()

conn.close()