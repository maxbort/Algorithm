import sys
input = sys.stdin.readline

n = int(input())
family = [[] for _ in range(n+1)]
a,b = map(int,input().split())
m = int(input())
for _ in range(m):
    c,d = map(int,input().split())
    family[c].append(d)
    family[d].append(c)

answer_list = [0]*(n+1) 

def dfs(a):
    for i in family[a]:
        if answer_list[i] == 0:
            answer_list[i] = answer_list[a] + 1
            dfs(i)
dfs(a)

if answer_list[b] != 0:
    print(answer_list[b])
else:
    print(-1)