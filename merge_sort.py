"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

def merge_sort(data):
    """
    Merge sort algorithm.

    Parameters:
    data (list): List of integers to be sorted.

    Yields:
    data (list): List of integers at each step of sorting.
    """
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
            yield list(data)

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
            yield list(data)

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            yield list(data)
    else:
        yield list(data)
