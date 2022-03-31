#use this program to delete table in mysql taht has been created
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",#root is the defult username for mysql
    password="LionKing123$",
    #name of database that just created
    database="sistemparkir"
)

cursor=mydb.cursor()
#DROP TABLE is the keyword, customers is the title of table that wanted to delete
delete_table_query="""DROP TABLE customers"""
cursor.execute(delete_table_query)
mydb.commit

