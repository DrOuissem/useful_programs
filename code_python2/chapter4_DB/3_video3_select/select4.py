import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute(''' SELECT * FROM Students WHERE AGE = 21
''')

results = c.fetchall()

for row in results:
    print("Name :", row[0], end=" ")
    print("Id :", row[1], end=" ")
    print("Age :", row[2], end=" ")
    print("Grade :", row[3], end=" ")
    print()

conn.commit()

conn.close()