import re
import numpy as np

# Use: python3 sol.py < data.txt
with open(0) as f:
    data = [list(x.strip()) for x in f.readlines()]
    print(np.array(data))

    count = 0
    # Search horizontally
    regex = r'XMAS'
    for line in data:
        count += len(re.findall(regex, ''.join(line)))
        count += len(re.findall(regex, ''.join(line[::-1])))

    # Search diagonally
    # This is kinda weird
    for i in range(-len(data)+1, len(data)+1):
        # Diagonal that goes from top left to bottom right
        diag = np.diag(data, k=i)
        # Diagonal that goes from bottom left to top right
        diag2 = np.diag(np.flipud(data), k=-i)
        count += len(re.findall(regex, ''.join(diag)))
        count += len(re.findall(regex, ''.join(diag[::-1])))
        count += len(re.findall(regex, ''.join(diag2)))
        count += len(re.findall(regex, ''.join(diag2[::-1])))

    # Search vertically
    for line in np.transpose(data):
        count += len(re.findall(regex, ''.join(line)))
        count += len(re.findall(regex, ''.join(line[::-1])))
    print(count)