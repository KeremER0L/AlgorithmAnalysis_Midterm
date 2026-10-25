# Algorithm Analysis - Midterm Project

This repository contains the midterm assignment for the Algorithm Analysis course. It includes the implementation and performance analysis of two sorting algorithms: **Insertion Sort** and **Merge Sort**.

## 📁 Project Structure

    AlgorithmAnalysis_Midterm/
    ├── README.md              # Project overview and instructions
    ├── REPORT.md              # Detailed theoretical and empirical analysis
    └── src/
        ├── insertion_sort.py  # Insertion Sort implementation & benchmark tests
        └── merge_sort.py      # Merge Sort implementation & benchmark tests

## ⚙️ Selected Algorithms

1. **Insertion Sort**: A simple, in-place comparison-based sorting algorithm. It is highly efficient for small or nearly sorted datasets but has a quadratic time complexity for larger datasets.
2. **Merge Sort**: A stable, divide-and-conquer sorting algorithm. It provides a guaranteed time complexity of O(n log n), making it highly efficient for large datasets.

## 🚀 How to Run

### Prerequisites
- Python 3.x must be installed on your system.

### Execution
Navigate to the root directory of the project in your terminal and run the following commands:

    # Run Insertion Sort benchmark
    python src/insertion_sort.py

    # Run Merge Sort benchmark
    python src/merge_sort.py

## 📊 Quick Complexity Summary

| Algorithm      | Best Case  | Average Case | Worst Case | Space Complexity | Stable |
|----------------|------------|--------------|------------|------------------|--------|
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes    |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)             | Yes    |
