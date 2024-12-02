import numpy as np
import heapq

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

def is_safe(i):
    inc = isInc(i)
    dec = isDec(i)

    return inc ^ dec and max(np.diff(i)) <= 3 and min(np.diff(i)) >= -3

with open('data.txt') as f:
    data = [ list(map(int, i.split(" "))) for i in f.read().splitlines()]
    safe = 0
    safe_2 = 0
    for i in data:
        # Part 1
        if is_safe(i):
            safe += 1
            # Part 2
            safe_2 += 1
        else:
            for j in range(len(i)):
                if is_safe(i[:j] + i[j+1:]):
                    safe_2 += 1
                    break

    print(safe)
    print(safe_2)
            