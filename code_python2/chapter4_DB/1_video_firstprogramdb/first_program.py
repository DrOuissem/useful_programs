import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

#c.execute("CREATE IF NOT EXISTS TABLE Students (Name TEXT, Id INTEGER, Grade REAL )")

c.execute("DROP TABLE IF EXISTS Students")
conn.commit()

conn.close()