import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

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
    test_sizes = [1000, 5000, 10000, 20000]
    print("--- MERGE SORT PERFORMANCE ANALYSIS ---\n")
    evaluate_performance(merge_sort, test_sizes)