"""
Created on Mon Mai 01 12:04:12 2023

@author:
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
"""


def bubble_sort(data):
    """
    Bubble sort algorithm.

    Parameters:
    data (list): List of integers to be sorted.

    Yields:
    tuple: Tuple containing the pass number, the list of integers at each step of sorting, 
           the indices that were swapped, and the indices that are sorted.
    """
    n = len(data)
    for pass_num in range(n):
        for i in range(n - pass_num - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                yield pass_num, list(data), (i, i + 1), list(range(n - pass_num, n))
        yield pass_num, list(data), (), list(range(n - pass_num, n))
