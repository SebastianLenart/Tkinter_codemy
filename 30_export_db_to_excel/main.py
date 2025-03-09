# pip3 install mysql-connector
# pip3 install mysql-connector-python
# pip3 install mysql-connector-python-rf
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import pymysql
import csv


root = Tk()
root.title("mysql")
root.geometry("400x400")



"""
napisze tylko funkcje ktra jest wywoywana przez button:

def write_to_csv(result):
    with open ("customers.csv", "a") as f:
    w = csv.writer(f, dialect="excel")
    for recortd in result:
        w.writerow(result)


"""




# mydb = pymysql.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "password123",
# )
# print(mydb)
#
# my_cursor = mydb.cursor()
# #my_cursor.execute("""CREATE DATABASE codemy""")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
#
# my_cursor.execute("""CREATE TABLE customers (
# first_name VARCHAR(255),
# last_name VARCHAR(255)
# """)
#
# tiitle_label = Label(root, text="db")
# tiitle_label.grid(row=0, column=0, columnspan=2, pady="10")



root.mainloop()
