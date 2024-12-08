import sys
from collections import defaultdict

def get_input():
    data = [list(i) for i in open(sys.argv[1]).read().splitlines()]
    return data

def get_freqs(grid):
    antenna_loc = set()
    freq = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                antenna_loc.add(complex(i, j))
                freq[grid[i][j]].append(complex(i, j))
    return antenna_loc, freq

def part1(antenna_loc, freqs, grid):
    antinode = set()
    for freq in freqs:
        for i in range(len(freqs[freq])):
            for j in range(len(freqs[freq])):
                if i == j: continue
                freq_i = freqs[freq][i]
                freq_j = freqs[freq][j]
                antinode.add( freq_i - (freq_j - freq_i) )
                antinode.add( freq_j - (freq_i - freq_j) )
    
    a = {node for node in antinode if node.real >= 0 and node.real < len(grid) and node.imag >= 0 and node.imag < len(grid[0]) }
    return len(a)

def main():
    grid = get_input()
    antenna_loc, freqs = get_freqs(grid)
    print(part1(antenna_loc, freqs, grid))

if __name__ == '__main__':
    main()