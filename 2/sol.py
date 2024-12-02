import numpy as np

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

def is_safe(arr):
    return isInc(arr) ^ isDec(arr) and max(np.diff(arr)) <= 3 and min(np.diff(arr)) >= -3

with open('data.txt') as f:
    data = [ list(map(int, i.split(" "))) for i in f.read().splitlines()]
    safe = 0
    safe_2 = 0
    for arr in data:
        if is_safe(arr):
            # Part 1
            safe += 1
            # Part 2
            safe_2 += 1
        else:
            for i in range(len(arr)):
                if is_safe(arr[:i] + arr[i+1:]):
                    safe_2 += 1
                    break

    print(safe)
    print(safe_2)
            