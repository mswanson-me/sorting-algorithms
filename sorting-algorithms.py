import numpy as np
import pandas as pd

min = 1
max = 500
numElements = 100

# DEFINE AND PRINT ARRAY
###############################

def generateArray(min, max, numElements):
    return np.random.randint(min, max, numElements)

arr = generateArray(min, max, numElements)

print("Here is the unsorted array: ")
print(arr)

# BUBBLE SORT
###############################

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

print("Here is the bubble sorted array: ")
bubbleSort(arr)

# MERGE SORT
###############################

# RECURSIVE FUNCTION

def mergeSort(arr):
    i = len(arr)
    mid = int(i/2)

    print(mid)

    if i <= 1:
        return arr

    left = arr[0:mid]
    right = arr[mid:]

    return merge(mergeSort(left), mergeSort(right))

# COMPARISON FUNCTION

def merge(left, right):
    sorted = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            sorted += left[leftIndex]
            leftIndex += 1
        else:
            sorted += right[rightIndex]
            rightIndex += 1

    while leftIndex < len(left):
        sorted += left[leftIndex]
        leftIndex += 1

    while rightIndex < len(right):
        sorted += right[rightIndex]
        rightIndex += 1

    return sorted

print("Here is the merge sorted array: ")
merged = mergeSort(arr)
print(merged)

# QUICK SORT
###############################

