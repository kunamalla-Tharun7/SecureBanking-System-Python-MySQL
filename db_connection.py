import mysql.connector

db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    database="bank_project",
    password="Tharun@19"
)

cur_obj=db_connection.cursor()
