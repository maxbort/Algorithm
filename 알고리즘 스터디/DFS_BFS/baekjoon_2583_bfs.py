import sys
from collections import deque
input = sys.stdin.readline

m,n,k = map(int,input().split())

box = [list(map(int,input().split())) for _ in range(k)]

graph = [[0 for _ in range(n)] for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in box:
    lx,ly = i[0],i[1]
    rx,ry = i[2],i[3]

    for i in range(lx,rx):
        for j in range(ly,ry):
            graph[j][i] = 1

volume = []
queue = deque()


for i in range(m):
    for j in range(n):
        print(i,j, "error point")
        if graph[i][j] == 0:
            v = 1
            graph[i][j] = 1
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        v += 1
                        queue.append((nx,ny))
            volume.append(v)
print(len(volume))
volume.sort()
for i in volume:
    print(i, end=' ')