from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    n = len(maps) - 1
    m = len(maps[0]) - 1
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            
            if mx > n or my > m or mx < 0 or my < 0:
                continue
            if maps[mx][my] == 0 :
                continue
            if maps[mx][my] == 1:
                maps[mx][my] = maps[x][y] + 1
                q.append((mx, my))
    
    answer = maps[n][m]
    if answer == 1:
        return -1
    else:
        return answer
    
