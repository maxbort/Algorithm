n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
       
        # for i in range(4):
        #    mx = x + dx[i]
        #    my = y + dy[i]
        #    dfs(mx,my)
        #    return True
        dfs(x + 1,y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer += 1
            
print(answer)                
