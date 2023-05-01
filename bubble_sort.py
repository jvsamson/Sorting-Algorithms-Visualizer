"""
Created on Mon Mai 01 12:04:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

def bubble_sort(data):
    """
    Bubble sort algorithm.

    Parameters:
    data (list): List of integers to be sorted.

    Yields:
    data (list): List of integers at each step of sorting.
    """
    n = len(data)
    for i in range(n):
        # Traverse through all array elements
        for j in range(0, n - i - 1):
            # Swap if current element is greater than next
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        yield data, (j, j + 1)
