import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(x,y,baby_shark): 
    dist = [[0] * n for _ in range(n)]
    visit = [[False] * n for _ in range(n)]

    que = deque()
    que.append((x,y))
    visit[x][y] = True
    temp = []

    while que:
        shark_x, shark_y = que.popleft()
        for i in range(4):
            nx = shark_x + dx[i]
            ny = shark_y + dy[i]
            
            if 0 <= nx < n and 0<= ny < n and not visit[nx][ny]:
                if graph[nx][ny] <= baby_shark:
                    que.append((nx,ny))
                    visit[nx][ny] = True
                    dist[nx][ny] = dist[shark_x][shark_y] + 1
                    
                    if graph[nx][ny] < baby_shark and graph[nx][ny] != 0:
                        temp.append((nx,ny,dist[nx][ny]))
                        
    temp.sort(key= lambda x : (-x[2],-x[0],-x[1])) # 크기, y좌표,x좌표로 정렬
    return temp

shark_x,shark_y = 0,0
baby_shark = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j

eat_cnt = 0
answer = 0

while True:
    shark = bfs(shark_x,shark_y,baby_shark)

    if len(shark) == 0:
        break
    
    nx,ny,distance = shark.pop()
    
    answer += distance
    
    graph[shark_x][shark_y],graph[nx][ny] = 0,0

    shark_x,shark_y = nx,ny

    eat_cnt += 1
    if eat_cnt == baby_shark:
        baby_shark += 1
        eat_cnt = 0
        
        
print(answer)
        

# 자기보다 몸집이 작은 물고기만 먹을 수 있고
# 자기 몸무게 만큼의 마릿수를 먹으면 성장
# 먹을 수 있는 물고기 많으면 가까운데 먼저
# 거리가 같을 시 더 위에 있는 것들
# 그것마저 같으면 더 왼쪽에 있는 것.