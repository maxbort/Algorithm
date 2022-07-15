import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())

graph = []
visit = [[False for _ in range(n)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if not visit[nx][ny] and graph[nx][ny] > h:
                visit[nx][ny] = True
                dfs(nx,ny,h) 
    
    
    
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))



cnt = 0
answer = 1
maxheight = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > maxheight:
            maxheight = graph[i][j]
            
for h in range(maxheight):
    visit = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visit[i][j]:
                cnt += 1
                visit[i][j] = True
                dfs(i,j,h)
    answer = max(answer,cnt)

print(answer)
     
