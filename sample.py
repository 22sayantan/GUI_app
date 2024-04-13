import tkinter as tk
import mysql.connector
from docx import Document

# Create the main application window:::
root = tk.Tk()
root.title("Display Data")

# set the window size:::
root.geometry("600x400")

# Custom Font:::
custom_font = ("Comic Sans MS",14)


# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Devil@123',
    database='study'
)

# Create a cursor object
cursor = conn.cursor()

# Query the database
cursor.execute("SELECT * FROM general_knowledge ORDER BY RAND() LIMIT 10")
rows = cursor.fetchall()

# Close the cursor and database connection
cursor.close()
conn.close()

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

for dicts in Ques_Set:
    Ques_var = ('Q) ',dicts['Ques'])
    ques = tk.Label(root,font=custom_font,text=Ques_var)
    ques.pack(anchor=tk.W)

    var = tk.IntVar()

    opt_1 = (' '*4,'A) ',dicts['opt_1'])
    opt_1 = tk.Radiobutton(root,font=custom_font,text=opt_1,variable=var,value=1)
    opt_1.pack(anchor=tk.W)
    opt_2 = (' '*4,'B) ',dicts['opt_2'])
    opt_2 = tk.Radiobutton(root,font=custom_font,text=opt_2,variable=var,value=2)
    opt_2.pack(anchor=tk.W)
    opt_3 = (' '*4,'C) ',dicts['opt_3'])
    opt_3 = tk.Radiobutton(root,font=custom_font,text=opt_3,variable=var,value=3)
    opt_3.pack(anchor=tk.W)
    opt_4 = (' '*4,'D) ',dicts['opt_4'])
    opt_4 = tk.Radiobutton(root,font=custom_font,text=opt_4,variable=var,value=4)
    opt_4.pack(anchor=tk.W)


root.mainloop()