import numpy as np

with open("sample.txt") as f:
    data = [list(map(int, i.split("   "))) for i in f.read().splitlines()]
    arr1, arr2 = np.array(data).T
    arr1.sort(), arr2.sort()
    print(sum( [abs(i-j) for (i, j) in zip(arr1, arr2)] ))
