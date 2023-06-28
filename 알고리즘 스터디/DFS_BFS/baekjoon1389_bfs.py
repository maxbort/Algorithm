from collections import deque
import sys
INF = float('inf')
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []
people = [[] for _ in range(n+1)]

for _ in range(m):
    graph.append(list(map(int,input().split())))

for i in graph:
    people[i[0]].append(i[1])
    people[i[1]].append(i[0])

answer = [INF]


    
for i in range(1,n+1):
    visit = [False for _ in range(n+1)]
    tot = 0
    q = deque()
    q.append([i,1])
    visit[i] = True
    while q:
        cur,cnt = q.popleft()
        for j in people[cur]:
            if not visit[j]:
                tot += cnt
                visit[j] = True
                q.append([j, cnt+1])
    answer.append(tot)

print(answer.index(min(answer)))