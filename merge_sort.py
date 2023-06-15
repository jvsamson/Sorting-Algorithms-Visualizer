"""
Created on Mon Mai 01 12:04:12 2023

@author:
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
"""

def merge_sort(data, level=0, sorted_indices=[]):
    """
    Merge sort algorithm.

    Parameters:
    data (list): List of integers to be sorted.

    Yields:
    tuple: List of integers at each step of sorting and range being merged.
    """
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        sorted_indices_left = yield from merge_sort(left_half, level=level+1)
        sorted_indices_right = yield from merge_sort(right_half, level=level+1)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i = i + 1
            else:
                data[k] = right_half[j]
                j = j + 1
            k = k + 1
            #yield level, data, list(range(len(data))), []
            yield level, data, list(range(len(data))), sorted_indices

        while i < len(left_half):
            data[k] = left_half[i]
            i = i + 1
            k = k + 1
            #yield level, data, list(range(len(data))), []
            yield level, data, list(range(len(data))), sorted_indices

        while j < len(right_half):
            data[k] = right_half[j]
            j = j + 1
            k = k + 1
            #yield level, data, list(range(len(data))), []
            yield level, data, list(range(len(data))), sorted_indices

        sorted_indices.extend(sorted_indices_left)
        sorted_indices.extend(sorted_indices_right)
    return sorted_indices
