import numpy as np

with open("data.txt") as f:
    data = [[int(j.strip()) for j in i.split("  ")] for i in f.read().splitlines()]
    arr1, arr2 = np.array(data).T
    print(sum( [abs(i-j) for (i, j) in zip(arr1, arr2)] ))

