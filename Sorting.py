"""
**SORTING** **ALGORITHMS**
"""

# Importing Libraries
import time
import random

# 1. Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# 2. Selection Sort
def selection_sort(arr):
    start=time.time()
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a
    end = time.time()
    return (end-start)

# 3. Insertion Sort
def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            A[i] = key
            i = i - 1

# 4. Merge Sort
def mergeSort(A):
    start = time.time()
    if len(A) > 1:
        mid = len(A) // 2                   # splitting array into tO  LEFT AND RIGHT
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)
        mergeSort(right)
        Merge(left, right, A)

def quick_sort(arr, low, high):
    i= low
    j = high
    p = arr[low + (high - low) // 2]
    while i <= j:
        while arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if low < j:
        quick_sort(arr, low, j)
    if i < high:
        quick_sort(arr, i, high)

arr = [random.randint(1, 10000) for _ in range(1000)]
start = time.perf_counter()
quick_sort(arr, 0, len(arr) - 1)
end = time.perf_counter()

print("Bubble Sort Time:", end - start, "seconds")
print("Selection Sort Time:", end - start, "seconds")
print("Insertion Sort Time:", end - start, "seconds")
print("Merge Time:", end - start, "seconds")
print("Heap Sort Time:", end - start, "seconds")