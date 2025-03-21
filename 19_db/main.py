from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("sliders")
root.geometry("400x700")

conn = sqlite3.connect('address_book.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS addresses (
first_name text,
last_name text,
address text,
city text,
state text,
zipcode integer
)""")


def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""
    UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    WHERE oid = :oid""",
              {
                "first": f_name_editor.get(),
                "last": l_name_editor.get(),
                "address": address_editor.get(),
                "city": city_editor.get(),
                "state": state_editor.get(),
                "zipcode": zipcode_editor.get(),
                "oid": record_id
              })
    conn.commit()
    conn.close()
    editor.destroy()



def edit():
    global editor
    editor = Tk()
    editor.title("editor")
    editor.geometry("400x400")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""SELECT * from addresses WHERE oid = """ + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    f_name_label_editor = Label(editor, text="first name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="last name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="city")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="state")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    save_btn = Button(editor, text="save record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("""DELETE from addresses WHERE oid= """ + delete_box.get())

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("""INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)""",
              {
                  "f_name": f_name.get(),
                  "l_name": l_name.get(),
                  "address": address.get(),
                  "city": city.get(),
                  "state": state.get(),
                  "zipcode": zipcode.get()
              })
    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("""SELECT *, oid from addresses""")
    records = c.fetchall()
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

f_name_label = Label(root, text="first name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="city")
city_label.grid(row=3, column=0)
state_label = Label(root, text="state")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="select ID")
delete_box_label.grid(row=9, column=0)

submit_btn = Button(root, text="Add record to db", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

edit_btn = Button(root, text="edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

conn.commit()
conn.close()

root.mainloop()
