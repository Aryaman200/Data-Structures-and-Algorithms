def rat_in_maze(maze):
    n = len(maze)
    res = []
    dx, dy = [1, 0], [0, 1]
    def backtrack(x, y, path):
        if x == n-1 and y == n-1:
            res.append(path[:])
            return
        for d in range(2):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                path.append((nx, ny))
                backtrack(nx, ny, path)
                path.pop()
                maze[nx][ny] = 1
    if maze[0][0] == 1:
        backtrack(0, 0, [(0, 0)])
    return res