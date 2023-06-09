# Sorting Algorithms Visualizer

This project visualizes the process of sorting a list of integers using two different sorting algorithms: Bubble Sort and Merge Sort. The aim is to provide an educational tool to help users understand the steps and performance of each algorithm.

## Features
- Generates a random list of integers to be sorted.
- Visualizes the sorting process step by step using a bar chart.
- Colors the bars to indicate the current state:
  - Gray: Unsorted
  - Red: Currently being compared or merged
  - Blue: Sorted and in the final position
- Displays the pass number (Bubble Sort) or level (Merge Sort) at each step.
- Calculates and displays the time complexity and actual time taken for sorting.


## Running the Application
To run the application, execute interface.py
As an example, you might enter the following:

- How many integers do you want to sort? **30**
- Enter the start of the range: **1**
- Enter the end of the range: **100**
- Which sorting algorithm do you want to use? (bubble/merge) **bubble**
- What delay time do you want? **0.3**

## Files
- [`bubble_sort.py`](https://github.com/jvsamson/Sorting-Algorithms-Visualizer/blob/main/bubble_sort.py): Contains the Bubble Sort algorithm implementation.
- [`merge_sort.py`](https://github.com/jvsamson/Sorting-Algorithms-Visualizer/blob/main/merge_sort.py): Contains the Merge Sort algorithm implementation.
- [`animation.py`](https://github.com/jvsamson/Sorting-Algorithms-Visualizer/blob/main/animation.py): Contains the functions to generate data and animate the sorting process using Matplotlib.
- [`interface.py`](https://github.com/jvsamson/Sorting-Algorithms-Visualizer/blob/main/interface.py): The main script to run the visualizer. Users can choose the sorting algorithm and specify the parameters for the list of integers.
