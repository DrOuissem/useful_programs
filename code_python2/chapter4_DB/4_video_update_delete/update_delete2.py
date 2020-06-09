import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute(''' DELETE FROM Students WHERE Id = 2233
''')


conn.commit()

conn.close()