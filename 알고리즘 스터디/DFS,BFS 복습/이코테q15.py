n, m, k, x = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [-1] * (n+1)
visited[x] = 0

def dfs(graph,visited,x):
    for i in graph[x]:
        if i == x:
            continue
        if visited[i] != 0:
            visited[i] = visited

dfs(graph,x,n,visited,0)
print(visited)
for i in range(n):
    if visited[i] == k:
        print(i)
    else:
        print(-1)
        break