import tkinter as tk #tkinter for gui , create window
from time import strftime #moduls fn ,curr time to string

# Function to update time AND Shw
def time():
    current_time = strftime('%H:%M:%S %p')  # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # Update every 1000ms (1 second)

# Create window
root = tk.Tk()
root.title("Digital CLK")

# Styling the label
label = tk.Label(root, font=('Arial', 50,"bold"), background='black', foreground='cyan')
label.pack(anchor='center')

time()  # Call the function once

# Start the GUI loop
root.mainloop()
