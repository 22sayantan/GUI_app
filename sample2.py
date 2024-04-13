import tkinter as tk
from tkinter import ttk
import mysql.connector

def fetch_data():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Devil@123",
        database="study"
    )
    cursor = conn.cursor()

    # Get the selected table from radio buttons
    table = selected_table.get()

    # Fetch MCQs from the selected table
    cursor.execute(f"SELECT * FROM {table} ORDER BY RAND() LIMIT 10")
    mcqs = cursor.fetchall()

    # Close the connection
    conn.close()

    # Display the fetched MCQs
    display_mcqs(mcqs)

def display_mcqs(mcqs):
    # Clear previous data
    for widget in mcq_widgets:
        widget.destroy()
    mcq_widgets.clear()

    # Display fetched MCQs
    for i, mcq in enumerate(mcqs, start=1):
        id,question, option1, option2, option3, option4,ans = mcq

        # Create a frame for the MCQ
        mcq_frame = tk.Frame(inner_frame)
        mcq_frame.pack(anchor="w", padx=10, pady=5)
        mcq_widgets.append(mcq_frame)

        # Display question
        question_label = tk.Label(mcq_frame, text=f"{i}. {question}")
        question_label.pack(anchor="w")

        # Create variables to track selected option
        selected_option = tk.StringVar()

        # Display options using radio buttons
        option1_button = tk.Radiobutton(mcq_frame, text=option1, variable=selected_option, value=option1)
        option1_button.pack(anchor="w")
        option2_button = tk.Radiobutton(mcq_frame, text=option2, variable=selected_option, value=option2)
        option2_button.pack(anchor="w")
        option3_button = tk.Radiobutton(mcq_frame, text=option3, variable=selected_option, value=option3)
        option3_button.pack(anchor="w")
        option4_button = tk.Radiobutton(mcq_frame, text=option4, variable=selected_option, value=option4)
        option4_button.pack(anchor="w")

        # Save the selected option in the list
        selected_options.append(selected_option)

# Create the Tkinter window
root = tk.Tk()
root.title("MCQ Display")

root.geometry("800x600")
# Radio buttons to select the MCQ set
selected_table = tk.StringVar()
selected_table.set("mcq_set1")  # Set default MCQ set selection

table_frame = tk.Frame(root)
table_frame.pack()

set1_button = tk.Radiobutton(table_frame, text="GK", variable=selected_table, value="general_knowledge")
set1_button.pack(side="left")
set2_button = tk.Radiobutton(table_frame, text="MCQ Set 2", variable=selected_table, value="mcq_set2")
set2_button.pack(side="left")

# Create a list to store selected options
selected_options = []

# Create a canvas and a scrollbar for MCQs
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to contain the MCQs
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Bind the canvas to the scrollbar
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_canvas_configure)

# Create a list to store MCQ widgets
mcq_widgets = []

# Button to fetch and display MCQs
fetch_button = tk.Button(root, text="Fetch MCQs", command=fetch_data)
fetch_button.pack()

root.mainloop()
