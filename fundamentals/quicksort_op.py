# implementation of quicksort with hoare partitioning
# help from https://pythonschool.net/data-structures-algorithms/code/quick_sort.py
import random

# swap two elements in a list
def swap(i, j, ls):
    tmp = ls[i]
    ls[i] = ls[j]
    ls[j] = tmp

# hoare partition
def partition(arr, lo, hi):
    piv = arr[lo]
    i = lo + 1
    j = hi

    while True:
        while i <= j and arr[i] < piv:
            i += 1
        while arr[j] >= piv and j >= i:
            j -= 1
        if j < i:
            break
        else:
            # swap places
            swap(i,j,arr)

    # swap start with arr[j]
    swap(lo,j,arr)
    if i == lo + 1:
        return -1
    else:
        return j

def quicksort(arr, lo, hi):
    if lo < hi:
        # partition the list
        pi = partition(arr, lo, hi)
        # sort both halves
        if pi == -1:
            return
        else:
            quicksort(arr, lo, pi - 1)
            quicksort(arr, pi + 1, hi)
