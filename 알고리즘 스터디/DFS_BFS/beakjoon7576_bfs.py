from collections import deque



box=[]
def bfs(box,a,b):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    day = -1

     
    while queue:
        day+=1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or box[nx][ny] == -1:
                    continue
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    queue.append((nx,ny))
    for i in box:
        if 0 in i:
            return -1             
    return day
                        


m,n = map(int,input().split())
queue = deque()
for i in range(n):
    box.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))
            
print(bfs(box,n,m))
            
