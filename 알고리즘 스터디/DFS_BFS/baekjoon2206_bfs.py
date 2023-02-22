import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
print(visited)
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [0,0,-1,1] 
dy = [-1,1,0,0]

def bfs(a,b,c):
    queue = deque()
    queue.append((a,b,c))

    while queue:
        x,y,z = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx,ny,1))
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx,ny,z))
    return -1

print(graph)
print(bfs(0,0,0))
print(visited)