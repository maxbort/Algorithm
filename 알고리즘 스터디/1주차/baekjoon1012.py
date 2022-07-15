from collections import deque

case = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                
    

for _ in range(case):
    cnt = 0
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                cnt+= 1
    print(cnt)
    
