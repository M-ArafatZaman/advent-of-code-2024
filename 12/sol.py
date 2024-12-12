from collections import deque

def get_perimeter(head, points):
    start_r, start_c = head
    total = 0
    q = deque([(start_r, start_c)])
    visited = set()
    while len(q) > 0:
        r, c = q.popleft()
        if (r, c) in visited: continue
        total += 4
        visited.add((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (r + dr, c + dc) in points and (r + dr, c + dc) not in visited:
                total -= 1
                q.append((r + dr, c + dc))
            elif (r + dr, c + dc) in visited:
                total -= 1
    return total

def part1(data):
    # Key is the head
    disjoint_sets: dict[set] = {}
    set_mp = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    for r in range(len(data)):
        for c in range(len(data[0])):
            if r == 0 and c == 0: 
                disjoint_sets[(r, c)] = set([(r, c)])
                set_mp[r][c] = (r, c)
            # Check up
            elif r - 1 >= 0 and data[r-1][c] == data[r][c] and (r-1,c):
                disjoint_sets[ set_mp[r-1][c] ].add((r, c))
                set_mp[r][c] = set_mp[r-1][c]
            # Check left
            elif c - 1 >= 0 and data[r][c-1] == data[r][c] and (r,c-1):
                disjoint_sets[ set_mp[r][c-1] ].add((r, c))
                set_mp[r][c] = set_mp[r][c-1]
            else:
                disjoint_sets[(r, c)] = set({(r, c)})
                set_mp[r][c] = (r, c)

            # Union join sets
            if r - 1 >= 0 and c - 1 >= 0 \
                and data[r-1][c] == data[r][c] == data[r][c-1] \
                and set_mp[r-1][c] != set_mp[r][c-1]:
                newHead = set_mp[r-1][c] if len(disjoint_sets[ set_mp[r-1][c] ]) > len(disjoint_sets[ set_mp[r][c-1] ]) else set_mp[r][c-1]
                oldHead = set_mp[r-1][c] if newHead == set_mp[r][c-1] else set_mp[r][c-1]
                for o_r, o_c in disjoint_sets[oldHead]:
                    set_mp[o_r][o_c] = newHead
                disjoint_sets[newHead] = disjoint_sets[newHead].union(disjoint_sets[oldHead])
                del disjoint_sets[oldHead]

    price = 0
    for head, points in disjoint_sets.items():
        price += len(points) * get_perimeter(head, points)
    return price

def main():
    data = open(0).read().splitlines()
    print(part1(data))

if __name__ == "__main__":
    main()