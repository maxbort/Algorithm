com = int(input())
pair = int(input()) 

net = [[] for _ in range(com+1)]

infection = 0

for _ in range(pair):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

visit = [False] * (com+1)
def dfs(a):
    global infection
    visit[a] = True
    for i in net[a]:
        if not visit[i]:
            dfs(i)
            infection+=1


dfs(1)
print(infection)
        
        