import tkinter as tk

def submit_form():
    # Get the values from the entry fields
    subjects = selected_subject.get() 
    
    # Display the submitted data (for demonstration purposes)
    print(f"Subject: {subjects}")

# Create the main application window
app = tk.Tk()
app.title("Simple Form Desktop Display")

# Create a label for the form
form_label = tk.Label(app, text="Please fill out the form:")
form_label.pack()

# Create a dropdown menu for subject selection:::
subject_label = tk.Label(app,text="Subjects:")
subject_label.pack()
selected_subject = tk.StringVar(app)
selected_subject.set("select subject")
subject_menu = tk.OptionMenu(app, selected_subject, "Networking","Economics","DSA")
subject_menu.pack()

# Create a button to submit the form
submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.pack()

# Start the main event loop
app.mainloop()
