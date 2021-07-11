import mysql.connector

tds = mysql.connector.connect(
    host="localhost",
    user="vahi",
    password="VaishnaV@9621",
    database = "dt"
)
si = tds.cursor()
si.execute("CREATE TABLE vall(name VARCHAR(255), employee_id VARCHAR(255), salary VARCHAR(200)")
sql = "INSERT INTO vall (name, employee_id, salary) values(%s,%s,%d)"
val = [("Ravi","im565",100000 ), ("Shyam","im65",250000), ("Radha","im232",665225 ),
       ("krishna","im21",300000 ), ("arjuna","im56",680000 )]
si.executemany(sql,val)
tds.commit()
si = tds.cursor()
si.execute("SHOW TABLES")
for value in si:
  print(value)
