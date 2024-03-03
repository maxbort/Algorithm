import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

apart = []
for _ in range(n):
    apart.append(list(map(int,input().rstrip())))


q = deque()
danji = 0

def bfs(i,j,q):
    count = 0
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if apart[nx][ny] == 1:
                    apart[nx][ny] = 0
                    count += 1
                    q.append((nx,ny))
                    
    return count

answer = []

for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            apart[i][j] = 0
            answer.append(bfs(i,j,q))

print(len(answer))
answer.sort()
for i in answer:
    print(i)