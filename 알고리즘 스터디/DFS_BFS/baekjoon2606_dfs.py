import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

computer = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)


def dfs(start):
    for i in computer[start]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)

    
dfs(1)

print(sum(visit)-1)