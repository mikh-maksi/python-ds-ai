import mysql.connector

mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="dbbase123connect",
  database="mikhmaksi2$default"
)

mycursor = mydb.cursor()

sql = 'TRUNCATE customers'
mycursor.execute(sql)

f = open('customers.csv', 'r')

elements_list = []
for line in f:
    element = line.split(';')
    element.pop()
    sql = f"INSERT INTO customers (name, address) VALUES ('{element[0]}', '{element[1]}')"
    print(sql)
    mycursor.execute(sql)



mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x) #Просматриваем часть элемента (по списку)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
