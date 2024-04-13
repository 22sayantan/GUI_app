import tkinter as tk
from tkinter import ttk
import mysql.connector

def get_input(event=None):
    user_input = entry.get()
    user_input_2 = entry2.get()
    print("User input:", user_input)
    print("User input:", user_input_2)

def get_purchase_input(event=None):
    input_1 = purchase_entry.get()
    input_2 = purchase_entry2.get()
    input_3 = purchase_entry3.get()
    print("User input:", input_1)
    print("User input:", input_2)
    print("User input:", input_3)

# Database Save to Database:::

    # connect to mysql database:::
    conn = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = 'Devil@123',
        database = 'mydb'
    )

    cursor = conn.cursor()

# Create the main window:::
root = tk.Tk()
root.title("Store Records")

# Create a Notebook (tabbed interface):::
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create tabs:::
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Sell')
notebook.add(tab2, text='Purchase')

# Tab_1: Create input field:::
label = tk.Label(tab1, text="product name : ")
label.pack()

entry = tk.Entry(tab1)
entry.pack()

label = tk.Label(tab1, text="sell price : ")
label.pack()

entry2 = tk.Entry(tab1)
entry2.pack()

    # Bind the Enter key to the entry field:::
entry2.bind("<Return>",get_input)

    # Button:::
button = tk.Button(tab1, text="Submit", command=get_input)
button.pack()

# Tab 2 content
label = tk.Label(tab2, text="product name : ")
label.pack()

purchase_entry = tk.Entry(tab2)
purchase_entry.pack()

label = tk.Label(tab2, text="Units : ")
label.pack()

purchase_entry2 = tk.Entry(tab2)
purchase_entry2.pack()

label = tk.Label(tab2, text="buy price : ")
label.pack()

purchase_entry3 = tk.Entry(tab2)
purchase_entry3.pack()

    # Bind the Enter key to the entry field:::
purchase_entry3.bind("<Return>",get_purchase_input)

    # Button:::
button = tk.Button(tab2, text="Submit", command=get_input)
button.pack()

# Run the Tkinter event loop:::
root.mainloop()