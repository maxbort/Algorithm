import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n,m = map(int,input().split())

graph = [[0 for _ in range(b)] for _ in range(a)]
orders = []
robot_xy = []

cnt = 1
for _ in range(n):
    x,y,dir = map(str,input().split())
    x,y = int(x)-1,int(y)-1
    graph[x][y] = cnt
    cnt+=1
    robot_xy.append([x,y,dir])
for _ in range(m):
    orders.append(list(map(str,input().split())))


for order in orders:
    robot_num, ord, rep = order
    robot_num = int(robot_num)
    robot_num -= 1
    
    robot_x, robot_y, robot_dir = robot_xy[robot_num]
    
    for _ in range(int(rep)):
        if ord == 'F':
            if robot_dir == 'E':
                if robot_x + 1 < a and graph[robot_x+1][robot_y] == 0:
                    graph[robot_x][robot_y], graph[robot_x+1][robot_y] =\
                        graph[robot_x+1][robot_y], graph[robot_x][robot_y]
                    robot_x += 1
                else:
                    if robot_x+1 >=a:
                        print("Robot {} crashes into the wall".format(robot_num+1))
                        sys.exit()
                    else:
                        print("Robot {0} crashes into robot {1}".format(robot_num+1,graph[robot_x+1][robot_y]))
                        sys.exit()
                        
            if robot_dir == 'W':
                if robot_x - 1 >= 0 and graph[robot_x-1][robot_y] == 0:
                    graph[robot_x][robot_y], graph[robot_x-1][robot_y] =\
                        graph[robot_x-1][robot_y], graph[robot_x][robot_y]
                    robot_x -= 1

                else:
                    if robot_x-1 < 0:
                        print("Robot {} crashes into the wall".format(robot_num+1))
                        sys.exit()
                    else:
                        print("Robot {0} crashes into robot {1}".format(robot_num+1,graph[robot_x-1][robot_y]))
                        sys.exit()
            if robot_dir == 'S':
                if robot_y - 1 >= 0 and graph[robot_x][robot_y-1] == 0:
                    graph[robot_x][robot_y], graph[robot_x][robot_y-1] =\
                        graph[robot_x][robot_y-1], graph[robot_x][robot_y]
                    robot_y -= 1
                else:
                    if robot_y-1 < 0:
                        print("Robot {} crashes into the wall".format(robot_num+1))
                        sys.exit()
                    else:
                        print("Robot {0} crashes into robot {1}".format(robot_num+1,graph[robot_x][robot_y-1]))
                        sys.exit()
        
        
            if robot_dir == 'N':
                if robot_y +1 < b and graph[robot_x][robot_y+1] == 0:
                    graph[robot_x][robot_y], graph[robot_x][robot_y+1] =\
                        graph[robot_x][robot_y+1], graph[robot_x][robot_y]
                    robot_y += 1
                else:
                    if robot_y+1 >=b:
                        print("Robot {} crashes into the wall".format(robot_num+1))
                        sys.exit()
                    else:
                        print("Robot {0} crashes into robot {1}".format(robot_num+1,graph[robot_x][robot_y+1]))
                        sys.exit()
        
        if ord == 'L':
            if robot_dir == 'E':
                robot_dir = 'N'
            elif robot_dir == 'W':
                robot_dir = 'S'
            elif robot_dir == 'N':
                robot_dir = 'W'
            else:
                robot_dir = 'E'
        if ord == 'R':
            if robot_dir == 'E':
                robot_dir= 'S'
            elif robot_dir == 'W':
                robot_dir = 'N'
            elif robot_dir == 'N':
                robot_dir = 'E'
            else:
                robot_dir = 'W'
    robot_xy[robot_num][0],robot_xy[robot_num][1],robot_xy[robot_num][2] =\
        robot_x,robot_y,robot_dir
            

print('OK')