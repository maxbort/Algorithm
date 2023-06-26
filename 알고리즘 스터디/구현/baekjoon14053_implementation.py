import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

n, m = map(int,input().split())
graph = []

robot = list(map(int,input().split()))

for _ in range(n):
    graph.append(list(map(int,input().split())))

x, y, d = robot
cnt = 0
while True:
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1
    check = False

    for i in range(4):
        if d != 0:
            nd = d - 1
        else:
            nd = 3
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                cnt += 1
                x = nx
                y = ny
                d = nd
                check = True
                break
        d = nd  
    if not check:
        if d == 2 or d == 3:
            nd = d - 2
        else:
            nd = d + 2
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0<= ny < m:
            if graph[nx][ny] != 1:
                x = nx
                y = ny
            else:
                break
        else:
            break    
print(cnt)
            
            
            
            
#                 if d == 0:
#                     if y-1 >=0:
#                         if graph[x][y-1] == 0:
#                             y -= 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             break
#                             # robot[0] = x
#                             # robot[1] = y
#                             # robot[2] = d
#                 elif d == 1:
#                     if x + 1 < n:
#                         if graph[x+1][y] == 0:
#                             x += 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             break
#                             # robot[0] = x
#                             # robot[1] = y
#                             # robot[2] = d
#                 elif d == 2:
#                     if y+1 < m:
#                         if graph[x][y+1] == 0:
#                             y += 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             break
 
#                 elif d == 3:
#                     if 0<= x-1:
#                         if graph[x-1][y] == 0:
#                             x -= 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             break

                            
#             else: # 청소 되지 않은 빈칸이 없는 경우
#                 if d == 0:
#                     if y+1 < m:
#                         if graph[x][y+1] == 1:
#                             check = False
#                             break

#                         else:
#                             y += 1
#                     else:
#                         check = False
#                         break
#                 elif d == 1:
#                     if 0 <= x-1:
#                         if graph[x-1][y] == 1:
#                             check = False
#                             break

#                         else:
#                             x -= 1
#                     else:
#                         check = False
#                         break
#                 elif d == 2:
#                     if 0< y-1:
#                         if graph[x][y-1] == 1:
#                             check = False
#                             break
                        
#                             # robot[0] = x
#                             # robot[1] = y
#                             # robot[2] = d
#                         else:
#                             y -= 1
#                     else:
#                         check = False
#                         break
#                 elif d == 3:
#                     if x+1 <= n:
#                         if graph[x+1][y] == 1:
#                             check = False
#                             break
#                         else:
#                             x += 1
#                     else:
#                         check = False
#                         break
                        
#                             # robot[0] = x
#                             # robot[1] = y
#                             # robot[2] = d
                        
            
            
# print(cnt)


# import sys
# input = sys.stdin.readline

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# n, m = map(int,input().split())
# graph = []

# robot = list(map(int,input().split()))

# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# x, y, d = robot
# graph[x][y] = 1
# cnt = 1
# check = True

# while True:
#     x,y,d = robot
#     if not check:
#         break
#     if graph[x][y] == 0:
#         graph[x][y] = 2
#         cnt += 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 0:
#                 if d != 0:
#                     d -= 1
#                 else:
#                     d = 3
#                 if d == 0:
#                     if y-1 >= 0:
#                         if graph[x][y-1] == 0:
#                             y -= 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             robot[0] = x
#                             robot[1] = y
#                             robot[2] = d
#                             break
#                 elif d == 1:
#                     if x + 1 < n:
#                         if graph[x+1][y] == 0:
#                             x += 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             robot[0] = x
#                             robot[1] = y
#                             robot[2] = d
#                             break
#                 elif d == 2:
#                     if y+1 < m:
#                         if graph[x][y+1] == 0:
#                             y += 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             robot[0] = x
#                             robot[1] = y
#                             robot[2] = d
#                             break
#                 elif d == 3:
#                     if 0 <= x-1:
#                         if graph[x-1][y] == 0:
#                             x -= 1
#                             graph[x][y] = 2
#                             cnt += 1
#                             robot[0] = x
#                             robot[1] = y
#                             robot[2] = d
#                             break
#             else:
#                 if d == 0:
#                     if y+1 < m:
#                         if graph[x][y+1] == 1:
#                             check = False
#                             break
#                         else:
#                             y += 1
#                     else:
#                         check = False
#                         break
#                 elif d == 1:
#                     if 0 <= x-1:
#                         if graph[x-1][y] == 1:
#                             check = False
#                             break
#                         else:
#                             x -= 1
#                     else:
#                         check = False
#                         break
#                 elif d == 2:
#                     if 0 < y-1:
#                         if graph[x][y-1] == 1:
#                             check = False
#                             break
#                         else:
#                             y -= 1
#                     else:
#                         check = False
#                         break
#                 elif d == 3:
#                     if x+1 <= n:
#                         if graph[x+1][y] == 1:
#                             check = False
#                             break
#                         else:
#                             x += 1
#                     else:
#                         check = False
#                         break
# print(cnt)



