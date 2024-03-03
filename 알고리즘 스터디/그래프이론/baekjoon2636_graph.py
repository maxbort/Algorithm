import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
graph = []
q = deque()

for _ in range(n):
    graph.append(list(map(int,input().split())))

visit = [[False for _ in range(m)] for _ in range(n)] 
cheeze_list =[]

def cheeze_melt():
    visit = [[False for _ in range(m)] for _ in range(n)]

    q.append((0,0))
    visit[0][0] = True
    cheeze_cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if graph[nx][ny] == 0:
                    visit[nx][ny] = True
                    q.append((nx,ny))
                else:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visit[nx][ny] = True
                        cheeze_cnt += 1
    cheeze_list.append(cheeze_cnt)
    return cheeze_cnt

time = 0
while True:
    time += 1
    answer = cheeze_melt()
    if answer == 0:
        break
print(time-1)         
print(cheeze_list[-2])

        