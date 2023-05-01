"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

def merge_sort(data, start=0, end=None):
    """
    Merge sort algorithm.

    Parameters:
    data (list): List of integers to be sorted.

    Yields:
    tuple: List of integers at each step of sorting and range being merged.
    """
    if end is None:
        end = len(data)
    
    if end - start > 1:
        mid = start + (end - start) // 2

        yield from merge_sort(data, start, mid)
        yield from merge_sort(data, mid, end)

        left_half = data[start:mid]
        right_half = data[mid:end]

        i = 0
        j = 0
        k = start

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
            yield data, (start, end)

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
            yield data, (start, end)

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            yield data, (start, end)
    else:
        yield data, (start, end)
