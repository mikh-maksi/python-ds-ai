# Создание базы данных
```py
import mysql.connector

mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="",
  database = "mikhmaksi2$default"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
```

Вставим элемент

```py
mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="",
  database = "mikhmaksi2$default"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

```

Вставим элемент в списке:

```py

mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="",
  database = "mikhmaksi2$default"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
```


