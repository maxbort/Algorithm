from collections import deque

n,k = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

dx = [-1,1,0,0] 
dy = [0,0,-1,1]


            
check = 0
def bfs(s):
    first = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                first.append((graph[i][j],i,j))
    queue = deque(sorted(first,key = lambda x : x[0]))
    check = 0
    while queue:
        if check == s:
            break
        for _ in range(len(queue)):
            virus, x, y = queue.popleft()
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if mx >= n or mx < 0 or my >= n or my < 0:
                    continue
                if graph[mx][my] == 0:
                    graph[mx][my] = virus
                    queue.append((virus,mx,my))
        
        check += 1

        
    
    

bfs(s)

print(graph[x-1][y-1])      