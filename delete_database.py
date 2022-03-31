import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",#root is the defult username for mysql
    password="LionKing123$",
    #name of database that just created
    database="sistemparkir"
)
cursor=mydb.cursor()
delete_database_query="""DROP DATABASE sistemparkir """
cursor.execute(delete_database_query)
mydb.commit