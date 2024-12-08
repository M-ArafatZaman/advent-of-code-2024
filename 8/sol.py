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
    part2 = set()
    for freq in freqs:
        for i in range(len(freqs[freq])):
            for j in range(len(freqs[freq])):
                if i == j: continue
                freq_i = freqs[freq][i]
                freq_j = freqs[freq][j]
                antinode.add( freq_i - (freq_j - freq_i) )
                antinode.add( freq_j - (freq_i - freq_j) )
                for k in range(len(grid)):
                    part2.add( freq_i - k*(freq_j - freq_i) )
                    part2.add( freq_j - k*(freq_i - freq_j) )
    
    filter_func = lambda x: x.real >= 0 and x.real < len(grid) and x.imag >= 0 and x.imag < len(grid[0])
    a = {i for i in antinode if filter_func(i)}
    b = {i for i in part2 if filter_func(i)}
    return len(b)

def main():
    grid = get_input()
    antenna_loc, freqs = get_freqs(grid)
    print(part1(antenna_loc, freqs, grid))

if __name__ == '__main__':
    main()