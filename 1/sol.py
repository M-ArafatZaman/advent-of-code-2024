import numpy as np
from collections import Counter

with open("sample.txt") as f:
    data = [list(map(int, i.split("   "))) for i in f.read().splitlines()]
    arr1, arr2 = np.array(data).T
    arr1.sort(), arr2.sort()
    c_arr2 = Counter(arr2)
    print(sum( [abs(i-j) for (i, j) in zip(arr1, arr2)] ))
    print(sum( [ i * c_arr2.get(i, 0) for i in arr1 ] ))
    