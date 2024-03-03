import sys

n,m = map(int,input().split())

stu = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    stu[a].append(b)

print(stu)
def dfs(start):
    visited[start] = True
    for i in stu[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    return

answer = 0
for i in range(1,n+1):
    visited = [False for _ in range(n+1)]
    visited[0] = True
    dfs(i)
    print(visited)
    if False in visited:
        continue
    else:
        answer+=1

print(answer)