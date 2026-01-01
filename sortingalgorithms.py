#insretion sort
from turtle import left
from turtledemo.sorting_animate import partition


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1],arr[j] = arr[j],arr[j-1] #swap
            j-=1 #until it reaches 0 it'll stop because j>0
#selection sort
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        cur_min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
                arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]
#merge sort/ divide and conquer
def merge_sort(arr):
    if len(arr)>1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
                    k+=1
            while i<len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k] = right[j]
                j+=1
                k+=1
#quick sort
def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i
import random
import time

ary = []
ary2 = []
ary3 = []
ary4 = []

for i in range(10000):
    r = random.randint(1, 10000)
    ary.append(r)
    ary2.append(r)
    ary3.append(r)
    ary4.append(r)

t1 = time.time()
quick_sort(ary, 0, len(ary) - 1)
t2 = time.time()
print("quick_sort time:", t2 - t1)

t1 = time.time()
insertion_sort(ary2)
t2 = time.time()
print("insertion_sort time:", t2 - t1)

t1 = time.time()
selection_sort(ary3)
t2 = time.time()
print("selection_sort time:", t2 - t1)

t1 = time.time()
merge_sort(ary4)
t2 = time.time()
print("merge_sort time:", t2 - t1)