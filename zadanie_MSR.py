import tkinter as tk  # Import the tkinter library for GUI development
from tkinter import ttk  # Import the themed tkinter widgets

root = tk.Tk()  # Create the main application window
root.title("Zadanie 7 z maszyn elektryczynch")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window
root.resizable(False, False)  # Disable window resizing

# Create a label widget
label_Sf = ttk.Label(root, text="Pole przekroju redzenia:")
label_Sf.grid(column=0, row=0, padx=10, pady=10, sticky='W')

entry_Sf = ttk.Entry(root)  # Create an entry widget for user input
entry_Sf.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="m\u00B2").grid(column=2, row=0,
                                     padx=10, pady=10, sticky='W')  # Unit label

root.mainloop()  # Start the Tkinter event loop
