import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def evaluate_performance(algorithm, sizes):
    print(f"{'Data Size':<15} | {'Best Case(s)':<15} | {'Worst Case(s)':<15} | {'Average Case(s)':<15}")
    print("-" * 69)
    
    for n in sizes:
        scenarios = {
            'best': list(range(n)),
            'worst': list(range(n, 0, -1)),
            'average': [random.randint(0, n) for _ in range(n)]
        }
        
        results = []
        for case_name, data in scenarios.items():
            test_data = data.copy()
            start = time.perf_counter()
            algorithm(test_data)
            duration = time.perf_counter() - start
            results.append(duration)
            
        print(f"{n:<15} | {results[0]:<15.4f} | {results[1]:<15.4f} | {results[2]:<15.4f}")

if __name__ == "__main__":
    test_sizes = [1000, 5000, 10000]
    print("--- INSERTION SORT PERFORMANCE ANALYSIS ---\n")
    evaluate_performance(insertion_sort, test_sizes)