import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(n)]
graph[0][0] = 1
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(visited)
def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0':
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])
