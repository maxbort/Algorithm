from collections import deque
import copy

def bfs():
    q = deque()
    test_lab = copy.deepcopy(lab)
    
    for i in range(n):
        for j in range(m):
            if test_lab[i][j] == 2:
                q.append((i,j))
                
    
        while q:
            x, y = q.popleft()
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                
                if mx < 0 or mx >= n or my < 0 or my >=m:
                    continue
                if test_lab[mx][my] == 0:
                    if test_lab[x][y] == 2:
                        test_lab[mx][my] = 2
                        q.append((mx, my))    
            
    global answer            
    temp = 0  
    for i in test_lab:
        temp += i.count(0)
        
    answer = max(answer, temp)   


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0



answer = 0
n,m = map(int,input().split())

lab = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

for _ in range(n):
    lab.append(list(map(int,input().split())))

wall(0) 
print(answer)
    




                            
    
    