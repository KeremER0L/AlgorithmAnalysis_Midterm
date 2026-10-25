# Sorting Algorithm Analysis

Algorithm Analysis Course — Midterm Assignment

## Project Structure

\`\`\`
AlgorithmAnalysis_Midterm/
├── README.md              # This file
├── REPORT.md              # Detailed project report (CPU/Memory analysis & Comparisons)
└── src/
    ├── insertion_sort.py  # Insertion Sort implementation with benchmarks
    └── merge_sort.py      # Merge Sort implementation with benchmarks
\`\`\`

## Selected Algorithms

1. **Insertion Sort** — A simple, intuitive comparison-based sorting algorithm that builds the final sorted array one item at a time. Excellent for nearly sorted data.
2. **Merge Sort** — A highly efficient, stable, divide-and-conquer sorting algorithm. Consistently performs in O(n log n) time across all cases.

## How to Run

### Prerequisites
- Python 3.x installed on your system.

### Execution
Navigate to the project root directory and run the scripts using Python:

\`\`\`bash
python src/insertion_sort.py
python src/merge_sort.py
\`\`\`

## Quick Complexity Summary

| Algorithm      | Best       | Average    | Worst      | Space    | Stable |
|----------------|------------|------------|------------|----------|--------|
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |