import mysql.connector
mydb = mysql.connector.connect( host="localhost", user= "vahi", password="VaishnaV@9621", database = "doc")
vi = mydb.cursor()
vi.execute("SHOW TABLES")
for value in vi:
  print(value)
vi= mydb.cursor()
sql = "INSERT INTO doctor (doctor_name,doctor_ID,patients) VALUES (%s, %s, %s)"
val = [("Dev","KM11","3"),("Diya","KM07","5"),("Abhi","KM15","2"),("Keshav","KM21","4"),("Devi","KM26","0")]
vi.executemany(sql,val)
mydb.commit()
sql = "SELECT * FROM doctor WHERE patients ='5'"
vi.execute(sql)
myresult = vi.fetchall()
for x in myresult:
  print(x)
sql = "SELECT * FROM doctor WHERE patients ='0'"
vi.execute(sql)
myresult = vi.fetchall()
for i in myresult:
    print(i)
