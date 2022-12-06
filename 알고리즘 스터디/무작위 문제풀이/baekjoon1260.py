N, M, V = map(int,input().split())

A = [[] for _ in range (N+1)]
for i in range(M):
    a,b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
    A[a].sort()
    A[b].sort()
queue=[]

# 방문 여부 체크
visit = [False]*(N+1)


#dfs와 bfs 정의
def dfs(V):
    print(V,end=' ')
    visit[V] = True
    for i in A[V]:
        if not visit[i]:
            dfs(i)
            
def bfs(V):
    queue.append(V)
    visit[V]=True
    while queue:
        a = queue.pop(0)
        print(a, end=' ')
        for i in A[a]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                
dfs(V)
visit = [False]*(N+1)

print()
bfs(V)