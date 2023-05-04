"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

import random
import time
import math
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
    pass_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    ax.set_xlim(0, len(data))
    ax.set_ylim(0, int(1.1*max(data)))

    def update_colors_bubble(swapped_indices, sorted_indices):
        color_array = ['gray'] * len(data)
        for i in swapped_indices:
            color_array[i] = 'red'
        for i in sorted_indices:
            color_array[i] = 'blue'
        for rect, color in zip(rects, color_array):
            rect.set_color(color)

    def update_colors_merge(compared_indices, sorted_indices):
        color_array = ['gray'] * len(data)
        for i in compared_indices:
            color_array[i] = 'red'
        for i in sorted_indices:
            color_array[i] = 'blue'
        for rect, color in zip(rects, color_array):
            rect.set_color(color)
    
    start_time = time.time()

    if sorting_algorithm == bubble_sort:
        ax.set_title('Bubble Sort (Time Complexity: O(n^2))')
        for pass_num, d, swapped_indices, sorted_indices in sorting_algorithm(data):
            pass_text.set_text(f'Pass: {pass_num}')
            for rect, val, text in zip(rects, d, texts):
                rect.set_height(val)
                text.set_text(str(val))
                text.set_position((text.get_position()[0], val))
            update_colors_bubble(swapped_indices, sorted_indices)
            fig.canvas.draw()
            plt.pause(delay)
    else:
        ax.set_title('Merge Sort (Time Complexity: O(n log n))')
        for level, d, compared_indices, sorted_indices in sorting_algorithm(data):
            pass_text.set_text(f'Level: {level}')
            for rect, val, text in zip(rects, d, texts):
                rect.set_height(val)
                text.set_text(str(val))
                text.set_position((text.get_position()[0], val))
            update_colors_merge(compared_indices, sorted_indices)
            fig.canvas.draw()
            plt.pause(delay)

    end_time = time.time()

    actual_time_taken = end_time - start_time 

    n = len(data)
    if sorting_algorithm == bubble_sort:
        time_complexity = f"O(n^2) = {n**2}"
    elif sorting_algorithm == merge_sort:
        time_complexity = f"O(n*log(n)) = {n * math.log2(n)}"

    ax.text(0.02, 0.90, f"Time Complexity: {time_complexity}", transform=ax.transAxes)
    ax.text(0.02, 0.85, f"Actual Time Taken: {actual_time_taken:.4f} seconds", transform=ax.transAxes)
    fig.canvas.draw()

    plt.show()
