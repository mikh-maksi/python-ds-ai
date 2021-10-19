# Чтение данных

```py
mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="1tmed1a123",
  database = "mikhmaksi2$default"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x) #Просматриваем все элементы
```

```py
mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="1tmed1a123",
  database = "mikhmaksi2$default"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0]) #Просматриваем часть элемента (по списку)
```

Используем WHERE в SELECT

```py
mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="1tmed1a123",
  database = "mikhmaksi2$default"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers WHERE address = 'Yellow Garden 2'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```