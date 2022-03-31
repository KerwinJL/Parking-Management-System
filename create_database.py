import mysql.connector

#the mydb can change to any thta you want
mydb= mysql.connector.connect(
  #can use localhost or ip adress
  host="localhost",
  #your own username
  user="root",
  # your own password when you download mysql,password anda apabila download mysql
  password="LionKing123$"
)

#cursor() method of a MySQLConnection object to create a cursor object to perform various SQL operations
#if you change mydb the mydb.cursor()also need to change
mycursor=mydb.cursor()
#use CREATE DATABSE to create a database and its title
mycursor.execute("CREATE DATABASE sistemparkir")