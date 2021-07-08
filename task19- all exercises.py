import mysql.connector
dtbs = mysql.connector.connect(host="localhost", user="vahi", password="VaishnaV@9621")
vai = dtbs.cursor()
vai.execute("CREATE TABLE stud(name VARCHAR(255), science VARCHAR(255), maths VARCHAR(255), english VARCHAR(255)")
sql = "INSERT INTO stud(name, science, maths, english) values(%s,%s,%s,%s)"
val = [("Ravi", "88", "85", "77"), ("Shyam", "66", "85", "87"), ("Radha", "89", "98", "83"),
       ("krishna", "90", "95", "87"), ("arjuna", "86", "75", "90")]
vai.executemany(sql, val)
dtbs.commit()
tel = "SELECT * FROM stud WHERE science LIKE '%9%' "
vai.execute(tel)
d = vai.fetchall()
for i in d:
    do = "INSERT INTO stop(nam VARCHAR(255))"
    up = ["i"]
    vai.execute(do, up)
kk = " SELECT * FROM stop "
vai.execute(kk)
o = vai.fetchall()
for x in o:
    print(x)
