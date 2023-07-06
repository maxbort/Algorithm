import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

q = deque()

visit = [False for _ in range(100001)]
count = [-1 for _ in range(100001)]

visit[n] = True
count[n] = 0
q.append(n)

while(q):
    a = q.popleft()
    
    if a == m:
        print(count[a])
        break
    if 0 <= a-1 < 100001 and not visit[a-1]:
        q.append(a-1)
        visit[a-1] = True
        count[a-1] = count[a] + 1
    if 0< 2*a < 100001 and not visit[2*a]:
        q.appendleft(2*a)
        visit[2*a] = True
        count[2*a] = count[a]
        
    if 0 < a+1 < 100001 and not visit[a+1]:
        q.append(a+1)
        visit[a+1] = True
        count[a+1] = count[a] + 1
        
    


# from collections import deque

# n, k = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
# q = deque()
# q.append(n) 
# visited = [-1 for _ in range(100001)]
# visited[n] = 0

# while q:
#     s = q.popleft()
#     if s == k:
#         print(visited[s])
#         break
#     if 0 <= s-1 < 100001 and visited[s-1] == -1:
#         visited[s-1] = visited[s] + 1
#         q.append(s-1)
#     if 0 < s*2 < 100001 and visited[s*2] == -1:
#         visited[s*2] = visited[s]
#         q.appendleft(s*2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
#     if 0 <= s+1 < 100001 and visited[s+1] == -1:
#         visited[s+1] = visited[s] + 1
#         q.append(s+1)

# q.append([[n-1,1], [n,0], [n+1,1]])

# while q:
#     a,b,c = q.popleft()
    
#     if a[0] == m:
#         print(a[1])
#         break
#     elif b[0] == m:
#         print(b[1])
#         break
#     elif c[0] == m:
#         print(c[1])
#         break
#     else:
#         q.append([[a[0]-1, a[1] + 1], [2*a[0], a[1]], [a[0] +1, a[1] + 1]])
#         q.append([[b[0]-1, b[1] + 1], [2*b[0], b[1]], [b[0] +1, b[1] + 1]])
#         q.append([[c[0]-1, c[1] + 1], [2*c[0], c[1]], [c[0] +1, c[1] + 1]])
    
    






# while True:
#    a = n*2
#    b = (n-1)*2
#    c = (n+1)*2
   
#    if 


