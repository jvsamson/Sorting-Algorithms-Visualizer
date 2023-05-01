"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

import tkinter as tk
from tkinter import simpledialog
from animation import generate_data, animate
from bubble_sort import bubble_sort
from merge_sort import merge_sort

root = tk.Tk()
root.withdraw()

# Prompt the user to enter the number of integers
n = simpledialog.askinteger("Input", "How many integers do you want to sort?", minvalue=1, maxvalue=100)

# Prompt the user to enter the range of integers
range_start = simpledialog.askinteger("Input", "Enter the start of the range:", minvalue=0)
range_end = simpledialog.askinteger("Input", "Enter the end of the range:", minvalue=range_start + 1)

# Prompt the user to choose the sorting algorithm
sorting_algorithm = simpledialog.askstring("Input", "Which sorting algorithm do you want to use? (bubble/merge)")

if sorting_algorithm == 'bubble':
    sorting_algorithm = bubble_sort
elif sorting_algorithm == 'merge':
    sorting_algorithm = merge_sort
else:
    raise ValueError("Invalid sorting algorithm. Choose 'bubble' or 'merge'.")

# Prompt the user to enter delay time
delay = simpledialog.askfloat("Input", "What delay time do you want?", minvalue=0.01)

# Generate data
data = generate_data(n, range_start, range_end)

# Animate
animate(data, delay, sorting_algorithm)
