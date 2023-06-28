import sys
from collections import deque

input = sys.stdin.readline

n,l,r = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))


def find_union(a,b):
    union = []
    que = deque()
    que.append((a,b))
    union.append((a,b))
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visit[nx][ny] = True
                    que.append((nx,ny))
                    union.append((nx,ny))
                    
    return union
                
answer = 0

while True:
    visit = [[False for _ in range(n+1)] for _ in range(n)]

    flag = False
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = True
                union = find_union(i,j)
            
                if len(union) > 1:
                    flag = True
                    tot = 0
                    for x, y in union:
                        tot += graph[x][y]
                    limit = tot//len(union)

                    for x,y in union:
                        graph[x][y]= limit
                        
    if not flag:
        break
    answer += 1
    
print(answer)