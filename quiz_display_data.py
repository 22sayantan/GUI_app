import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

def selected_options(event):
    selected_value = drop_var.get()
    print(selected_value)

def show_selected():
        selected_option = var.get()
        print(fruit_list[selected_option-1])
def display_data():
    # connect to mysql database
    conn = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = 'Devil@123',
        database = 'study'
    )

    cursor = conn.cursor()

    # Create variable with table name:::
    My_Table = 'general_knowledge'

    # Fetch 10 random row:::
    sql = f"SELECT * FROM {My_Table} ORDER BY RAND() LIMIT 8"
    cursor.execute(sql)

    rows = cursor.fetchall()    # Fetch rows from the result:::
    conn.close()         # Close connection:::

    # fetch data from database :::
    Ques_Set = []
    for row in rows:
        mcq_dict = {}
        # mcq_dict['id'] = row[0]
        mcq_dict['Ques'] = row[1]
        mcq_dict['opt_1'] = row[2]
        mcq_dict['opt_2'] = row[3]
        mcq_dict['opt_3'] = row[4]
        mcq_dict['opt_4'] = row[5]
        Ques_Set.append(mcq_dict)
    # print(Ques_Set)   

    for i,dicts in enumerate(Ques_Set,start=1):
        # question,option_1,option_2,option_3,option_4 = mcq
        text.insert(tk.END,f"{i}. {dicts['Ques']}\n")
        text.insert(tk.END,f"  A) {dicts['opt_1']}\n")
        text.insert(tk.END,f"  B) {dicts['opt_2']}\n")
        text.insert(tk.END,f"  C) {dicts['opt_3']}\n")
        text.insert(tk.END,f"  D) {dicts['opt_4']}\n")
# Create the main application window:::
root = tk.Tk()
root.title("Display Data")

# set the window size:::
root.geometry("800x600")

# Custom Font:::
custom_font = ("Times New Roman",14)

# Create a text widget
text = tk.Text(root,font=custom_font,width='77')
text.pack()


# create a button to save data:::
fetch_button = tk.Button(root, text="Fetch Data",font=custom_font, command=display_data)
fetch_button.pack(padx=10, pady=5,side=tk.BOTTOM)
'''
# get pdf button:::
get_pdf_button = tk.Button(root,font=custom_font, text="Get Pdf")
get_pdf_button.pack(padx=10, pady=5,side=tk.BOTTOM)
'''
# Run the application:::
root.mainloop()