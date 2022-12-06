from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while queue:
        z,y,x = queue.popleft()
        visit[z][y][x] = True
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and not visit[nz][ny][nx]:
                if graph[nz][ny][nx] == 0:
                    queue.append((nz,ny,nx))
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    visit[nz][ny][nx] = True


m,n,h=map(int,input().split())
# m = x n = y h = z
graph = []
queue = deque()

visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
    graph.append(tmp)

for i in range(h): #z
    for j in range(n): #y
        for k in range(m):#x
            if graph[i][j][k] == 1:
                queue.append((i,j,k))    
    
bfs()

cnt = 0
check = False
for k in range(h):
    for j in range(n):
        for i in range(m):
            if graph[k][j][i] == 0:
                check = True
            cnt = max(cnt, graph[k][j][i])
if check:
    print(-1)
else:
    print(cnt-1)
