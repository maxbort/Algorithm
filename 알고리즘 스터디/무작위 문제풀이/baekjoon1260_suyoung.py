# DFS BFS 문제
from collections import deque

# dfs
n, m, v = map(int, input().split())

# 예제 입력을 받기 위해서 2차원 배열 형태로 밭고 n+1인 이유는 0부터 시작하니까 0인 부분을 나두고 1부터 n까지 받으려고하는것
graph = [[] * (n+1) for _ in range(n+1)]

# 배열의 입력을 잘 2개씩 받기 위함
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visitied = [False] * (n+1)
# visited를 공유하면 뒤의 함수가 실행이 잘 되지 않는다.
visitiedS = [False] * (n+1)


def dfs(now):
    visitied[now] = True
    print(now, end='')

    for i in graph[now]:
        if not visitied[i]:
            dfs(i)


def bfs(now):
    queue = deque([now])
    visitiedS[now] = True

    while queue:
        v = queue.popleft()
        print(v, end='')

        for i in graph[v]:
            if not visitiedS[i]:
                queue.append(i)
                visitiedS[i] = True


# print(dfs(v)) 이런식으로 하면 마지막에 None이 발생하는데 이를 조심
dfs(v)
print()
bfs(v)
