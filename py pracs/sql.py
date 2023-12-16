import sqlite3

mydb=sqlite3.connect('test.db')
c=mydb.cursor()

ct="CREATE TABLE IF NOT EXISTS Students (SAP_ID INTEGER, NAME TEXT, AGE INTEGER)"
c.execute(ct)
SAP_ID=79279
NAME='SHARAN'
AGE=22


# insert
n="INSERT INTO Students VALUES (?,?,?)"
c.execute(n,(SAP_ID,NAME,AGE))

c.execute("INSERT INTO Students VALUES(6003,'Sha',19)")

# display
temp=[]
d="SELECT * FROM Students"
c.execute(d)

temp=c.fetchall()
for i in temp:
    print(i)

c.execute(d)    
print(c.fetchone())

c.execute(d)    
print(c.fetchmany())

c.execute(d)    
print(c.fetchall())