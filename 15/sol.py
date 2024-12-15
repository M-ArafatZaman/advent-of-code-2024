
def main():
    grid, moves = open(0).read().split("\n\n")
    moves = ''.join(moves.splitlines())
    grid = list(map(list, grid.splitlines()))
    robot_r, robot_c = [ (r, c) for c in range(len(grid[0])) for r in range(len(grid)) if grid[r][c] == '@'][0]

    move_dir = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1), 
    }
    last_moved = True
    for m in range(len(moves)):
        # Skip consecutive null moves
        if not last_moved and moves[m] == moves[m-1]: continue
        dr, dc = move_dir[moves[m]]
        move = False
        if 0 <= robot_r + dr < len(grid) and 0 <= robot_c + dc < len(grid[0]):
            if grid[robot_r + dr][robot_c + dc] == '.':
                move = True
            elif grid[robot_r + dr][robot_c + dc] == 'O':
                # DFS Attempt
                nr, nc = robot_r + dr, robot_c + dc
                while grid[nr][nc] != '#' and not move:
                    if grid[nr][nc] == 'O':
                        nr, nc = nr + dr, nc + dc
                    elif grid[nr][nc] == '.':
                        move = True
                        grid[nr][nc] = 'O'
        if move:
            grid[robot_r][robot_c] = '.'
            robot_r += dr
            robot_c += dc
            grid[robot_r][robot_c] = '@'
            last_moved = True
        else:
            last_moved = False

    #print('\n'.join([''.join(row) for row in grid]))
    print(sum([ 100*r + c for c in range(len(grid[0])) for r in range(len(grid)) if grid[r][c] == 'O' ]))


if __name__ == "__main__":
    main()