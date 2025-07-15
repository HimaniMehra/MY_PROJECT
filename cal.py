import tkinter as tk

# Function to update expression in the entry field
def press(num):
    entry_var.set(entry_var.get() + str(num))

# Function to evaluate the expression
def equalpress():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry field
def clear():
    entry_var.set("")

# Create GUI window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=clear).grid(row=row, column=col, columnspan=4, sticky='we')
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()
