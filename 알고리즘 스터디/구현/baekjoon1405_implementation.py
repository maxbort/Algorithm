import sys
from collections import deque
input = sys.stdin.readline

# 왔던 곳을 한번이라도 지나칠 경우 -> 단순 x
# 가는 곳이 전부 처음일 경우 -> 단순
# 모든 경로마다 확률 계산하면서 지나감
# 모든 경우에 대해서 전부 확인
# 횟수가 채워지면 리턴.

def move(x,y,per,cnt):
    global tot
    if cnt == n:
        tot += per
        return
    
    a = per
    robot_map[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2*n + 1 and 0<= ny < 2*n + 1:
            if robot_map[nx][ny] == 1:
                continue
            else:
                move(nx,ny,a*d_per[i],cnt+1)
                robot_map[nx][ny]= 0 

n, e_per, w_per, s_per, n_per = map(int,input().split())

robot_map = [[[0] for _ in range(2*n + 1)] for _ in range(2*n + 1)]
e_per /= 100
w_per /= 100
s_per /= 100
n_per /= 100

d_per = [e_per,w_per,s_per,n_per]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
tot = 0

                
move(n,n,1,0)
print(tot)
