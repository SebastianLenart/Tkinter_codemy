# pip3 install mysql-connector
# pip3 install mysql-connector-python
# pip3 install mysql-connector-python-rf
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import pymysql

root = Tk()
root.title("mysql")
root.geometry("400x400")

"""

Nieprzydatne informacje tutaj sa !
Nieprzydatne informacje tutaj sa !
Nieprzydatne informacje tutaj sa !

"""

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
)
print(mydb)

my_cursor = mydb.cursor()
#my_cursor.execute("""CREATE DATABASE codemy""")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

my_cursor.execute("""CREATE TABLE customers (
first_name VARCHAR(255),
last_name VARCHAR(255)
""")




root.mainloop()
"""
nie mam czasu na ogarnianie czemu baza danych mi nie dziala, kiedys jak bede uzywal tej bazy to sie wdroze w to 


"""