import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

length = 100001
route = [0] * length
visit = [False] * length

route[n] = 0
visit[n] = True
q = deque()
q.append(n)

while q:
    a = q.popleft()
    
    if 2*a <= length and not visit[2*a]:
        q.appendleft(2*a)
        visit[2*a] = True
        route[2*a] = route[a]
        
    if a+1 <= length-1 and not visit[a+1]:
        q.append(a+1)
        visit[a+1] = True
        route[a+1] = route[a] + 1
        
    if 0 <= a-1 and not visit[a-1]:
        q.append(a-1)
        visit[a-1] = True
        route[a-1] = route[a] + 1
        
print(route[m])