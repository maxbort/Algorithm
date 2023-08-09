import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
    
    
N,R,Q = map(int,input().split())

edge = []

for _ in range(N-1):
    edge.append(list(map(int,input().split())))    

graph = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
U = []
U.append(int(input()))

for i in edge:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])


def cnt_node(check):
    answer[check] = 1
    for i in graph[check]:
        if answer[i] == 0:
            cnt_node(i)
            answer[check] += answer[i]
cnt_node(R)
print(answer)
# for i in U:
#     print(answer[i])
    
