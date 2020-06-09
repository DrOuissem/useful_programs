import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute('''CREATE IF NOT EXISTS TABLE Students 
          (Name TEXT, Id INTEGER PRIMARY KEY, AGE INTEGER, Grade REAL )''')

c.execute(''' INSERT INTO Students ('NAME', 'Id','AGE','Grade')
VALUES ('MOHAMED',3233,20,91.5)
''')

c.execute(''' INSERT INTO Students ('NAME', 'Id','AGE','Grade')
VALUES ('HANEN',4233,20,91.5)
''')

conn.commit()

conn.close()