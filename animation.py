"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

import random
import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
from merge_sort import merge_sort

def generate_data(n, range_start, range_end):
    """
    Generate a list of n integers between range_start and range_end.

    Parameters:
    n (int): Number of integers.
    range_start (int), range_end (int): Range of integers.

    Returns:
    list: List of n integers.
    """
    return random.sample(range(range_start, range_end), n)

def animate(data, delay, sorting_algorithm):
    """
    Animate the sorting of data using a specified sorting algorithm.

    Parameters:
    data (list): List of integers to be sorted.
    delay (float): Delay between each step in seconds.
    sorting_algorithm (function): Sorting algorithm to be used.
    """
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(data)), data, align='edge')

    ax.set_xlim(0, len(data))
    ax.set_ylim(0, int(1.1*max(data)))

    for d in sorting_algorithm(data):
        for rect, val in zip(rects, d):
            rect.set_height(val)
        fig.canvas.draw()
        plt.pause(delay)

    plt.show()
