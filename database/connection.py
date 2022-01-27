import mysql.connector

myconn = mysql.connector.connect(host ="localhost",user ="root",passwd = "root")

print(myconn)

cur = myconn.cursor()

print(cur)
try:
    dbs = cur.execute("show databases")
except:
    myconn.rollback()

for x in cur:
    print(x)
myconn.close()

print(cur)