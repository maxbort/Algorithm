import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

root = [0] * (n+1)

def dfs(graph, v, root):
    for i in graph[v]:
        if root[i] == 0:
            root[i] = v
            dfs(graph,i,root)
dfs(graph,1,root)

for i in range(2,n+1):
    print(root[i])    