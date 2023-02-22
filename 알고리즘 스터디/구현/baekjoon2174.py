import sys

input = sys.stdin.readline

a,b = map(int,input().split())
n,m = map(int,input().split())



graph = [[0 for _ in range(a)] for _ in range(b)]
robots = []
orders = []

r_n = 1

for _ in range(n):
    x,y,dir = map(str,input().split())
    x = int(x) - 1
    y = int(y) - 1
    graph[y][x] = r_n
    robots.append([x, y,dir])
    r_n += 1

for _ in range(m):
    r,order,cnt = map(str,input().split())
    r = int(r)-1
    cnt = int(cnt)
    orders.append([r,order,cnt])

print(graph)

for r, order, cnt in orders:
    if order == 'F':
        for _ in range(cnt):
            graph[robots[r][1]][robots[r][0]] = 0
            dx = robots[r][0]
            dy = robots[r][1]
            if robots[r][2] == 'E':
                dx += 1
                robots[r][0] = dx
                print("dx ,dy = ", dx,dy)
                print(robots)
            elif robots[r][2] == 'W':
                dx -= 1
                robots[r][0] = dx
                print("dx ,dy = ", dx,dy)
                print(robots)

            elif robots[r][2] == 'S':
                dy -= 1
                robots[r][1] = dy
                print("dx ,dy = ", dx,dy)
                print(robots)

            elif robots[r][2] == 'N':
                dy += 1
                robots[r][1] = dy
                print("dx ,dy = ", dx,dy)
                print(robots)
            
            
            if dx >= a or dx < 0 or dy >= b or dy < 0:
                print("Robot {} crashes into the wall".format(r+1))
                print(dx,dy)
                exit()
            if graph[dy][dx] != 0:
                print("Robot {0} crashes into robot {1}".format(r+1,graph[dy][dx]))
                exit()


            
            graph[dy][dx] = r+1

            for i in graph:
                print(i)

            

    elif order == 'L':
        for _ in range(cnt):
            if robots[r][2] == 'E':
                robots[r][2] = 'N'
            elif robots[r][2] == 'W':
                robots[r][2] = 'S'
            elif robots[r][2] == 'S':
                robots[r][2] = 'E'
            elif robots[r][2] == 'N':
                robots[r][2] = 'W'
    elif order == 'R':
        for _ in range(cnt):
            if robots[r][2] == 'E':
                robots[r][2] == 'S'
            elif robots[r][2] == 'W':
                robots[r][2] == 'N'
            elif robots[r][2] == 'S':
                robots[r][2] == 'W'
            elif robots[r][2] == 'N':
                robots[r][2] == 'E'
        
        

print(graph)
print(orders)