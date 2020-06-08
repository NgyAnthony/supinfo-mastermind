import random

# default array example
arr = ['x', 'x', 'x', 'x']

def place(arr, color, pos):
    # raplace array postion by color
    arr[pos] = color
    return arr

def arrGeneration(arr):
    # iterate on arr to replace x by random num
    for idx, value in enumerate(arr):
        arr[idx] = random.randint(0,5)
    return arr
