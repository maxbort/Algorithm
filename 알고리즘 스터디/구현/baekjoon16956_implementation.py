import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pas = [list(map(str,input().rstrip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if pas[i][j] == 'S':
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if pas[ni][nj] == 'W':
                        print(0)
                        exit()
                    else:
                        if pas[ni][nj] != 'S':
                            pas[ni][nj] = 'D'

print(1)
for i in pas:
    print("".join(i))