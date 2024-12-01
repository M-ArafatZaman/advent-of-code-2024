import numpy as np
from collections import Counter

with open("data.txt") as f:
    data = [[int(j.strip()) for j in i.split("  ")] for i in f.read().splitlines()]
    arr1, arr2 = np.array(data).T
    c_arr2 = Counter(arr2)
    print(sum( [ i * c_arr2.get(i, 0) for i  in arr1 ] ))
