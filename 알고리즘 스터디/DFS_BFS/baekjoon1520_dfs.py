import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
dy = [0,0,-1,1]
dx = [1,-1,0,0]

for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
        
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y]=0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx,ny)

    return dp[x][y]
                
print(dfs(0,0))

# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10