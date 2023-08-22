import sys
input = sys.stdin.readline

mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
#visit = [[False for _ in range(m)] for _ in range(n)]
visit = [[False] * m for _ in range(n)]

# for _ in range(n):
#     graph.append(list(map(int,input().split())))
answer = 0

def check_answer(x,y,c,cnt):
    global answer
    if cnt == 4:
        answer = max(answer,c)
        return
    for a in range(4):
        nx = x + mv[a][0]
        ny = y + mv[a][1]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = True
            check_answer(nx,ny,c+graph[nx][ny],cnt+1)
            visit[nx][ny] =False


def f(x,y):
    global answer

    for a in range(4):
        t = graph[x][y]
        for b in range(3):
            k = (a+b)%4
            nx = x + mv[k][0]
            ny = y + mv[k][1]
            if not (0 <= nx < n and 0 <= ny < m):
                t = 0
                break
            t += graph[nx][ny]
        answer = max(answer,t)


    

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        check_answer(i,j,graph[i][j],1)
        visit[i][j] = False

        f(i,j)


print(answer)