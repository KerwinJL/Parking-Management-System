import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",#root is the defult username for mysql
    password="LionKing123$",
    #name of database that just created
    database="sistemparkir"
)
mycursor=mydb.cursor()
#use CREATE TABLE to create a table and title as customers and under customers have to information which is nombor_carplate and masa_mula parkir
#VARCHAR in MySQL is a data type used for storing text
mycursor.execute("CREATE TABLE customers (id int PRIMARY KEY AUTO_INCREMENT, nombor_carplate VARCHAR(255), jenis_kenderaan VARCHAR(255), masa_mula_parkir VARCHAR(255))")