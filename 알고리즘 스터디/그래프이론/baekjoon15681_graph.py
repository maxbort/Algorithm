import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
    
N,R,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def cnt_node(check):
    answer[check] = 1
    for i in graph[check]:
        if answer[i] == 0:
            cnt_node(i)
            answer[check] += answer[i]
cnt_node(R)
for i in range(Q):
    print(answer[int(input())])
