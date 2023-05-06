"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

from animation import generate_data, animate
from bubble_sort import bubble_sort
from merge_sort import merge_sort

# Prompt the user to enter the number of integers
n = int(input("How many integers do you want to sort? (min: 1, max: 100)"))
if n < 1 or n > 100:
    raise ValueError

# Prompt the user to enter the range of integers
range_start = int(input("Enter the start of the range (min: 1):"))
range_end = int(input("Enter the end of the range (must be greater than start of range):"))
if range_start < 1 or range_end < range_start + 1:
    raise ValueError

# Prompt the user to choose the sorting algorithm
sorting_algorithm = input("Which sorting algorithm do you want to use? (bubble/merge)")

if sorting_algorithm == 'bubble':
    sorting_algorithm = bubble_sort
elif sorting_algorithm == 'merge':
    sorting_algorithm = merge_sort
else:
    raise ValueError("Invalid sorting algorithm. Choose 'bubble' or 'merge'.")

# Prompt the user to enter delay time
delay = float(input("What delay time do you want? (minimum value: 0.01)"))
if delay < 0.01:
    raise ValueError

# Generate data
data = generate_data(n, range_start, range_end)

# Animate
animate(data, delay, sorting_algorithm)
