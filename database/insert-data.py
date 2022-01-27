import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pythondb")

# creating the cursor object
cur = myconn.cursor()
sql = "insert into emp(name, id, salary) values (%s, %s, %s)"
val = ("John", 102, 25000)

# Creating a table with name Employee having four columns i.e., name, id, salary, and department id
dbs = cur.execute(sql,val)
myconn.commit()

for x in cur:
    print(x)
print(cur.rowcount,"records inserted")
myconn.close()