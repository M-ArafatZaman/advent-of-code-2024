import sys
from collections import deque

def score(grid, start_r, start_c):
    q = deque([(start_r, start_c)])
    visited = set()
    score = 0
    while len(q) > 0:
        r, c = q.popleft()
        if (r, c) in visited: continue
        visited.add((r, c))
        if grid[r][c] == 9 and (r, c): 
            score += 1
            continue
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
                if grid[r + dr][c + dc] - grid[r][c] == 1:
                    q.append((r + dr, c + dc))
    return score        

def part1(grid):
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                total += score(grid, r, c)
    return total

def main():
    grid = [list(map(int, i)) for i in open(sys.argv[1]).read().splitlines()]
    print(part1(grid))

if __name__ == "__main__":
    main()