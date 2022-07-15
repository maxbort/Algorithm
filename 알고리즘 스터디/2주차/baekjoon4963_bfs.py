from collections import deque

dx = [1, 1, 0,-1,-1,-1,0,1]
dy = [0,-1,-1,-1, 0,1,1,1]

def bfs(sea,a,b):
    queue = deque()
    queue.append((a,b))
    sea[a][b] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y +dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if sea[nx][ny] == 1:
                    sea[nx][ny] = 0
                    queue.append((nx,ny))
                    


while True:
    w,h= map(int,input().split())
    if w == 0 and h == 0:
        break
    sea = []
    cnt = 0
    for _ in range(h):
        sea.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if sea[i][j] == 1:
                bfs(sea,i,j)
                cnt += 1
    print(cnt)

    