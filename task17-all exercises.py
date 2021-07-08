# Exercise 1
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="vahi",
  password="VaishnaV@9621",
 database= "mydatabase"
)

dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)
import sqlite3
print( sqlite3.version)

# Exercise 2
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="vahi",
  password="VaishnaV@9621",
  database="mydatabase"
)

dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse :
  print(value)
dbse= mydb.cursor()

sql = "INSERT INTO customers (Employee_name, Employee_dep) VALUES (%s, %s)"
val = [("John", "Welding"), ('Amy', 'engines'),
  ('Hannah', 'procurement'),
  ('Michael', 'product management'),
  ('Sandy', 'sap'),
  ('Betty', 'innovation'),
  ('Richard', 'tires'),
  ('Susan', 'brakes'),
  ('Vicky', 'design'),
  ('Ben', 'frame'),
  ('William', 'steering'),
  ('Chuck', 'sales'),
  ('Viola', 'frame')]
dbse.executemany(sql, val)
mydb.commit()
print(dbse.rowcount, "record inserted.")
# Exercise 3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="vahi",
  password="VaishnaV@9621",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute(
        '''SELECT
                Column_One
                --,Column_Two
            FROM mydatabase.table''')

final_result = [list(i) for i in mycursor.fetchall()]
