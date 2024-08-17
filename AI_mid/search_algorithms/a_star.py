import heapq

def a_star_search(maze, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    priority_queue = [(0 + heuristic(start, goal), 0, start, [start])]  # (f_score, g_score, current_position, path)
    visited = set()

    while priority_queue:
        (f_score, g_score, current_position, path) = heapq.heappop(priority_queue)
        if current_position in visited:
            continue
        visited.add(current_position)

        x, y = current_position
        if current_position == goal:
            return path  # return the path when the goal is reached

        # Get the possible moves (up, down, left, right)
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            if is_valid_move(maze, neighbor) and neighbor not in visited:
                g = g_score + 1
                f = g + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (f, g, neighbor, path + [neighbor]))

    return None  # return None if no path is found

def is_valid_move(maze, position):
    x, y = position
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '0'
