import sys
from collections import defaultdict

def get_input():
    data = [list(i) for i in open(sys.argv[1]).read().splitlines()]
    return data

def get_freqs(grid):
    freqs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                freqs[grid[i][j]].append(complex(i, j))
    return freqs

def solve(freqs, grid):
    part1 = set()
    part2 = set()
    for freq in freqs:
        for i in range(len(freqs[freq])):
            for j in range(len(freqs[freq])):
                if i == j: continue
                freq_i = freqs[freq][i]
                freq_j = freqs[freq][j]
                # Part 1
                part1.add( freq_i - (freq_j - freq_i) )
                part1.add( freq_j - (freq_i - freq_j) )
                # Part 2
                for k in range(len(grid)):
                    part2.add( freq_i - k*(freq_j - freq_i) )
                    part2.add( freq_j - k*(freq_i - freq_j) )
    
    filter_func = lambda x: x.real >= 0 and x.real < len(grid) and x.imag >= 0 and x.imag < len(grid[0])
    a = {i for i in part1 if filter_func(i)}
    b = {i for i in part2 if filter_func(i)}
    return len(a), len(b)

def main():
    grid = get_input()
    freqs = get_freqs(grid)
    print(solve(freqs, grid))

if __name__ == '__main__':
    main()