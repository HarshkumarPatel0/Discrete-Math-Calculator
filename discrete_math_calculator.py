import tkinter as tk
import math

def calculate_permutations():
    n = int(entry_n.get())
    r = int(entry_r.get())
    result = math.perm(n, r)
    lbl_result["text"] = f"Permutations: {result}"

def calculate_combinations():
    n = int(entry_n.get())
    r = int(entry_r.get())
    result = math.comb(n, r)
    lbl_result["text"] = f"Combinations: {result}"

def calculate_factorial():
    n = int(entry_n.get())
    result = math.factorial(n)
    lbl_result["text"] = f"Factorial: {result}"

# Create the main window
window = tk.Tk()
window.title("Discrete Math Calculator")

# Create labels and entry fields
lbl_n = tk.Label(window, text="n:")
lbl_n.pack()

entry_n = tk.Entry(window)
entry_n.pack()

lbl_r = tk.Label(window, text="r:")
lbl_r.pack()

entry_r = tk.Entry(window)
entry_r.pack()

lbl_result = tk.Label(window, text="")
lbl_result.pack()

# Create buttons
btn_permutations = tk.Button(window, text="Calculate Permutations", command=calculate_permutations)
btn_permutations.pack()

btn_combinations = tk.Button(window, text="Calculate Combinations", command=calculate_combinations)
btn_combinations.pack()

btn_factorial = tk.Button(window, text="Calculate Factorial", command=calculate_factorial)
btn_factorial.pack()

# Run the GUI main loop
window.mainloop()
