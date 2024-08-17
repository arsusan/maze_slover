def is_valid_move(maze, position):
    x, y = position
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '0'

def visualize_maze(maze, path, start, goal):
    maze_copy = [row[:] for row in maze]
    for (x, y) in path:
        maze_copy[x][y] = '*'
    maze_copy[start[0]][start[1]] = 'S'
    maze_copy[goal[0]][goal[1]] = 'G'
    for row in maze_copy:
        print(' '.join(row))
