from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx,ny))
                
                
                
                            
        
    
    
    
n = int(input())
visit = [[False] * n for _ in range(n)]
graph=[]
cnt = 0
cnt2 = 0
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
            cnt+=1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visit = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
            cnt2+=1

print(cnt)
print(cnt2)