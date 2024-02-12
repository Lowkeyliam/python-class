import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")



conn.execute("INSERT INTO EMPLOYEES VALUES (111,'LIAM MAINA',19,600000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (121,'KERRY MUGWERU',18,500000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (131,'JAMES MWANGI',19,50000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (141,'SOIULJA BOY',30,30000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (151,'BIG MAC',25,20000.00)")
conn.commit()


print("Employee inserted successfully")
conn.close()