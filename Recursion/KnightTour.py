
def knight_tour(N):
    sol = [[-1]*N for _ in range(N)]
    moves = [(2, 1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
    def solve(x, y, movei):
        if movei == N*N:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0<=nx<N and 0<=ny<N and sol[nx][ny] == -1:
                sol[nx][ny] = movei
                if solve(nx, ny, movei+1): return True
                sol[nx][ny] = -1
        return False
    sol[0][0] = 0
    if solve(0,0,1):
        return sol
    return None