from collections import defaultdict, deque

with open(0) as f:
    grid = [list(i) for i in f.read().splitlines()]
    r, c = 0, 0
    for _r in range(len(grid)):
        for _c in range(len(grid[0])):
            if grid[_r][_c] in {"^"}:
                r, c = _r, _c

    visited = defaultdict(bool)
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


    print(len(visits))

