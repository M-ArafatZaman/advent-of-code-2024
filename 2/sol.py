import numpy as np
from itertools import accumulate

def isInc(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True

def isDec(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
    return True

with open('data.txt') as f:
    data = [ list(map(int, i.split(" "))) for i in f.read().splitlines()]
    safe = 0
    for i in data:
        inc = isInc(i)
        dec = isDec(i)

        if inc ^ dec and max(np.diff(i)) <= 3 and min(np.diff(i)) >= -3:
            safe += 1

    print(safe)
            