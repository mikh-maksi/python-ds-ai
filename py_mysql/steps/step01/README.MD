# Создание БД
В **Pythonanywhere** создаем БД. Далее - подключаемся к ней.
Устанавливаем модуль mysql.connector
`pip3 install mysql-connector-python`
```py
import mysql.connector

mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password=""
)

print(mydb)
```

Просматриваем доступные базы данных

```py
import mysql.connector

mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

```
Подключаемся непосредственно к БД.

```py
import mysql.connector

mydb = mysql.connector.connect(
  host="mikhmaksi2.mysql.pythonanywhere-services.com",
  user="mikhmaksi2",
  password="",
  database="mikhmaksi2$default"
)


```