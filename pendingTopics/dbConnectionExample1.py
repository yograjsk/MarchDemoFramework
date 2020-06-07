import sqlite3

connection = sqlite3.connect('mytestdb.db')

# connection.execute("CREATE TABLE STUDENT (ROLLNUMBER INT NOT NULL, NAME TEXT NOT NULL, AGE INT);")
# connection.execute("""CREATE TABLE STUDENT
#         (ROLLNUMBER INT NOT NULL,
#         NAME TEXT NOT NULL,
#         AGE INT);""")

connection.execute("""INSERT INTO STUDENT (ROLLNUMBER, NAME, AGE) VALUES (3, 'SURESH', 23)""")
connection.commit()

records = connection.execute("select * from STUDENT")
for i in records:
    print(i)
# print(records)





