from collections import deque
n = int(input())

apart = []
answer =[]

dy = [-1,1,0,0]
dx = [0,0,-1,1]


for _ in range(n):
    apart.append(list(map(int,input())))
    

def bfs(apart,a,b):
    queue = deque()
    queue.append((a,b))
    apart[a][b] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        apart[x][y] = 0 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if apart[nx][ny] == 1:
                apart[nx][ny] = 0
                queue.append((nx,ny))
                cnt+=1
            
    return cnt


for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            tot = bfs(apart,i,j)
            answer.append(tot)
answer.sort()

print(len(answer))
for i in answer:
    print(i)
    
    
