from collections import defaultdict, deque, Counter

dir_mp = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}
turn_vec = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

def is_loop(grid, r, c, gr, gc):
    visited = defaultdict(bool)
    q = deque([(r, c, "^")])
    while len(q) > 0:
        r, c, g = q.popleft()
        dr, dc = dir_mp[g]
        if visited[(r, c, g, dr, dc)]:
            return True
        visited[(r, c, g, dr, dc)] = True
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            if grid[r + dr][c + dc] == "#" or (r + dr == gr and c + dc == gc):
                q.append((r, c, turn_vec[g]))
                continue
            elif grid[r + dr][c + dc] == ".":
                q.append((r + dr, c + dc, g))
    return False

with open(0) as f:
    grid = [list(i) for i in f.read().splitlines()]
    r, c = 0, 0
    for _r in range(len(grid)):
        for _c in range(len(grid[0])):
            if grid[_r][_c] in {"^"}:
                r, c = _r, _c
    
    start_r, start_c = r, c

    # Part 1
    visited = defaultdict(bool)
    q = deque([(r, c, grid[r][c])])
    grid[r][c] = '.'
    visits = set([])
    while len(q) > 0:
        r, c, g = q.popleft()
        if visited[(r, c, g)]:
            continue
        visited[(r, c, g)] = True
        visits.add((r, c))
        dr, dc = dir_mp[g]
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            if grid[r + dr][c + dc] == "#":
                q.append((r, c, turn_vec[g]))
                continue
            elif grid[r + dr][c + dc] == ".":
                q.append((r + dr, c + dc, g))
    
    # Part 2
    count2 = 0
    for r, c in visits:
        if grid[r][c] == "#":
            continue
        if r == start_r and c == start_c:
            continue
        if is_loop(grid, start_r, start_c, r, c):
            count2 += 1

    print(len(visits))
    print(count2)