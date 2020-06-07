import sqlite3

connection = sqlite3.connect('mySample.db')

cursor = connection.cursor()

CreateTableQuery = """CREATE TABLE IF NOT EXISTS
STUDENT(ROLLNUMBER INGEGER NOT NULL, NAME TEXT NOT NULL, AGE INTEGER)"""
cursor.execute(CreateTableQuery)

cursor.execute("INSERT INTO STUDENT VALUES (01, 'RAMESH', 21)")
cursor.execute("INSERT INTO STUDENT VALUES (02, 'SURESH', 22)")
cursor.execute("INSERT INTO STUDENT VALUES (03, 'JAYESH', 23)")
cursor.execute("INSERT INTO STUDENT VALUES (04, 'NARESH', 24)")

cursor.execute("select * from STUDENT")

results = cursor.fetchall()
print(results)
