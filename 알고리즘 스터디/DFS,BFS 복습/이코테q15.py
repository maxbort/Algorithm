n, m, k, x = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [-1] * m

result =0
def dfs(graph,x,n,visited,result):
    visited[x] = result
    
    for i in range(n):
        if visited[i] != 0:
            result+=1
            dfs(graph,i,n,visited,result)

dfs(graph,x,n,visited,0)
print(visited)
for i in range(n):
    if visited[i] == k:
        print(i)
    else:
        print(-1)
        break