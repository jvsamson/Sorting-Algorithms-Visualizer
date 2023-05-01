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
    color_array = ['gray'] * len(data)
    rects = ax.bar(range(len(data)), data, color=color_array)
    texts = [ax.text(i, v, str(v)) for i, v in enumerate(data)]
    annotation = ax.annotate('', xy=(0,0), xytext=(-20,20), textcoords="offset points",
                             bbox=dict(boxstyle="round", fc="w"),
                             arrowprops=dict(arrowstyle="->"))
    annotation.set_visible(False)

    ax.set_xlim(0, len(data))
    ax.set_ylim(0, int(1.1*max(data)))

    def update_colors_bubble(indices):
        color_array = ['gray'] * len(data)
        for i in indices:
            color_array[i] = 'red'
        for rect, color in zip(rects, color_array):
            rect.set_color(color)

    def update_colors_merge(indices):
        color_array = ['gray'] * len(data)
        for i in range(indices[0], indices[1]):
            color_array[i] = 'red'
        for rect, color in zip(rects, color_array):
            rect.set_color(color)

    def update_annotation_bubble(ind, val):
        x,y = ind, val
        annotation.xy = (x, y)
        text = f"Comparing: {data[ind]} and {data[ind+1]}"
        annotation.set_text(text)
        annotation.set_visible(True)

    if sorting_algorithm == bubble_sort:
        for d, indices in sorting_algorithm(data):
            for rect, val, text in zip(rects, d, texts):
                rect.set_height(val)
                text.set_text(str(val))
                text.set_position((text.get_position()[0], val))
            update_colors_bubble(indices)
            if indices:
                update_annotation_bubble(indices[0], data[indices[0]])
            fig.canvas.draw()
            plt.pause(delay)
    else:
        for d, indices in sorting_algorithm(data):
            for rect, val, text in zip(rects, d, texts):
                rect.set_height(val)
                text.set_text(str(val))
                text.set_position((text.get_position()[0], val))
            update_colors_merge(indices)
            fig.canvas.draw()
            plt.pause(delay)

    plt.show()
