from collections import deque


def bfs(a):
    queue = deque()
    queue.append(a)
    visit[a] = True
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 0
for i in range(1,n+1):
    if not visit[i]:
        if not graph[i]:
            cnt+=1
            visit[i]=True
        else:
            bfs(i)
            cnt+=1

print(cnt)