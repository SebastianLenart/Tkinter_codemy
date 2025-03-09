from tkinter import ttk



drop = ttk.Combobox(search_customers, value=["Search by...", "Last name", "Email address"])
drop.current(0)
drop.pack() # ...

selected = drop.get() # ...
if selected == "Search by...":
    print("Search by...") 