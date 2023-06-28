import sys

input = sys.stdin.readline

v,e = map(int,input().split())

tree = [list(map(int,input().split())) for _ in range(e)]

tree.sort(key=lambda x : x[2])

visit = [False] * (v+1)
visit[0] = True
answer = 0
for s,e,m in tree:
    if not visit[e]:
        answer += m
        visit[s] = True
        visit[e] = True
    
    if False not in visit:
        print(answer)
        break
    