import tkinter as tk  # Import the tkinter library for GUI development
# from tkinter import ttk  # Import the themed tkinter widgets
from ttkbootstrap import ttk  # Import ttk from ttkbootstrap for enhanced styling
from ttkbootstrap import Style

root = tk.Tk()  # Create the main application window

style = Style(theme="darkly")  # Apply a Bootstrap theme for better aesthetics

root.title("Zadanie 7 z maszyn elektryczynch")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window
root.resizable(False, False)  # Disable window resizing

Sf_var = tk.StringVar()  # Variable to store the cross-sectional area input
Sf_var.set("0.0025")  # Set default value for cross-sectional area
lf_var = tk.StringVar()  # Variable to store the average magnetic line length input
lf_var.set("0.8")  # Set default value for average magnetic line length

# Create a label widget
label_Sf = ttk.Label(root, text="Pole przekroju redzenia:")
label_Sf.grid(column=0, row=0, padx=10, pady=10, sticky='W')
# Bind the label to the Sf_var variable


entry_Sf = ttk.Entry(root)  # Create an entry widget for user input
entry_Sf.grid(column=1, row=0, padx=10, pady=10)
entry_Sf.configure(textvariable=Sf_var)  # Link the entry to Sf_var

ttk.Label(root, text="m\u00B2").grid(column=2, row=0,
                                     padx=10, pady=10, sticky='W')  # Unit label

# Create a label widget
label_lf = ttk.Label(root, text="Średnia długość linii magnetycznej:")
label_lf.grid(column=0, row=1, padx=10, pady=10, sticky='W')

# Bind the label to the lf_var variable


entry_lf = ttk.Entry(root)  # Create an entry widget for user input
entry_lf.grid(column=1, row=1, padx=10, pady=10)
entry_lf.configure(textvariable=lf_var)  # Link the entry to lf_var

ttk.Label(root, text="m").grid(column=2, row=1,
                               padx=10, pady=10, sticky='W')  # Unit label


def oblicz_window(parent):
    try:
        Sf_value = float(Sf_var.get())
        top = tk.Toplevel(parent)
        top.title("Wynik obliczeń")
        top.geometry("300x150")
        ttk.Label(top, text=f"Wartość Sf wynosi: {Sf_value} m²").pack(
            padx=10, pady=10)
        ttk.Button(top, text="Zamknij", command=top.destroy).pack(pady=10)
    except ValueError:
        print("Proszę wprowadzić poprawną wartość liczbową dla Sf.")


button_calculate = ttk.Button(root, text="Oblicz")  # Create a button widget
button_calculate.grid(column=0, row=2, padx=10, pady=20, columnspan=3)
button_calculate.config(
    command=lambda: oblicz_window(root))  # Set button command
button_calculate.config(bootstyle="danger")
root.mainloop()  # Start the Tkinter event loop
