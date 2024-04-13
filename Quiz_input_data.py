import tkinter as tk
import mysql.connector

def save_to_database():
    # connect to mysql database
    conn = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = 'Devil@123',
        database = 'mydb'
    )

    cursor = conn.cursor()

    # Create variable with table name:::
    My_Table = 'FormData'
    # Create table if not exists:::
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {My_Table}
                 (id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(255),
                 email VARCHAR(255),
                 age INT)''')

    # Insert data into the table:::
    sql = f"INSERT INTO {My_Table} (Question,option_1,option_2,option_3,option_4) VALUES (%s,%s,%s)"
    val = (name_entry.get(),email_entry.get(), int(age_entry.get()))
    cursor.execute(sql, val)

    # Commit changes and close connection:::
    conn.commit()
    conn.close()

    # Clear form fields
    ques_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    age_entry.delete(0, tk.END)

# Create the main window:::
root = tk.Tk()
root.title("Form Input")

# Create Custom Font :::
custom_font = ('Comic Sans MS',14)

# Create form labels and entry fields:::
ques_label = tk.Label(root,font=custom_font, text='Question: ')
ques_label.grid(row=0,column=0,padx=5,pady=5)
ques_entry = tk.Entry(root,font=custom_font, width=100)
ques_entry.grid(row=1,column=0,padx=5,pady=5)

ques_label_2 = tk.Label(root,font=custom_font, text='Option 1: ')
ques_label_2.grid(row=2,column=0,padx=5,pady=5)
ques_entry_2 = tk.Entry(root,font=custom_font, width=100)
ques_entry_2.grid(row=3,column=0,padx=5,pady=5)

ques_label_3 = tk.Label(root,font=custom_font, text='Option 2: ')
ques_label_3.grid(row=4,column=0,padx=5,pady=5)
ques_entry_3 = tk.Entry(root,font=custom_font, width=100)
ques_entry_3.grid(row=5,column=0,padx=5,pady=5)

ques_label_4 = tk.Label(root,font=custom_font, text='Option 3: ')
ques_label_4.grid(row=6,column=0,padx=5,pady=5)
ques_entry_4 = tk.Entry(root,font=custom_font, width=100)
ques_entry_4.grid(row=7,column=0,padx=5,pady=5)

ques_label_5 = tk.Label(root,font=custom_font, text='Option 4: ')
ques_label_5.grid(row=8,column=0,padx=5,pady=5)
ques_entry_5 = tk.Entry(root,font=custom_font, width=100)
ques_entry_5.grid(row=9,column=0,padx=5,pady=5)

correct_answer_label = tk.Label(root,font=custom_font, text=' Answer: ')
correct_answer_label.grid(row=10,column=0,padx=5,pady=5)
correct_answer_entry = tk.Entry(root,font=custom_font, width=100)
correct_answer_entry.grid(row=11,column=0,padx=5,pady=5)

# create a button to save data:::
save_button = tk.Button(root,font=custom_font, width=10, text='Save', command=save_to_database)
save_button.grid(row=12,column=0)

exit_button = tk.Button(root,font=custom_font, width=10, text='Exit', command=quit)
exit_button.grid(row=13,column=0)
# Run the application:::
root.mainloop()