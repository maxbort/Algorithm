from collections import deque

f,s,g,u,d = map(int,input().split())

count = [-1] * (f+1)

q = deque()
q.append(s)
count[s] = 0
while q:
    point = q.popleft()

    if point == g:
        print(count[point])
        exit()

    move_point1 = point + u
    move_point2 = point - d

    if 0< move_point1 <=f and count[move_point1] == 0:
        q.append(move_point1)
        count[move_point1] = count[point] + 1
    if 0 < move_point2 <= f and count[move_point2] == 0:
        q.append(move_point2)
        count[move_point2] = count[point] + 1
print("use the stairs")



