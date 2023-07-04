import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
graph=[]
visit=[[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

q = deque()
area = [0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]:
            visit[i][j] = True
            q.append((i,j))
            temp = 1
            while q:
                x,y = q.popleft()
                
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    
                    if 0<= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 1 and not visit[nx][ny]:
                            temp+=1 
                            visit[nx][ny] = True
                            q.append((nx,ny))
            area.append(temp)

print(len(area)-1)
print(max(area))
                    