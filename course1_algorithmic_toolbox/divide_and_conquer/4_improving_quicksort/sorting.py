# Uses python3
import sys
import random

def partition3(a, left, right):
    #write your code here
    pivot = a[left]
    mid1, mid2 = left, right
    i = left
    while i <= mid2:
        if a[i] < pivot:
            a[i], a[mid1] = a[mid1], a[i]
            mid1 += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[mid2] = a[mid2], a[i]
            mid2 -= 1
        else:
            i += 1
            
    return mid1, mid2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    mid1, mid2 = partition3(a, l, r)
    randomized_quick_sort(a, l, mid1 - 1)
    randomized_quick_sort(a, mid2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
