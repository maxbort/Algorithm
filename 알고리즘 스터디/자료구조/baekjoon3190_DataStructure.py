import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    a,b = map(int,input().split())
    a,b = a-1, b-1
    graph[a][b] = 1


l = int(input())
commands = []
for _ in range(l):
    commands.append(list((map(str,input().split()))))

s_dir = 'E'
snake = deque()
snake.append((0,0))
answer = 0

for command in commands:
    count, dir = int(command[0]),command[1]

    count -= answer
    for _ in range(count):
        if s_dir == 'E':
            head_x, head_y = snake.popleft()
            new_snake_x,new_snake_y = head_x, head_y+1
            answer += 1
            if (new_snake_x,new_snake_y) in snake:
                print(answer)
                exit()
            if 0 <= new_snake_x < n and 0 <= new_snake_y < n:
                if graph[new_snake_x][new_snake_y] == 1:
                    graph[new_snake_x][new_snake_y] = 0
                    snake.appendleft((head_x,head_y))                    
                    snake.appendleft((new_snake_x,new_snake_y))
                else:
                    snake.appendleft((head_x,head_y))
                    snake.appendleft((new_snake_x,new_snake_y))
                    snake.pop()
            else:
                print(answer)
                exit()
        elif s_dir == 'N':
            head_x, head_y = snake.popleft()
            new_snake_x,new_snake_y = head_x-1, head_y
            answer+= 1
            if (new_snake_x,new_snake_y) in snake:
                print(answer)
                exit()
            if 0 <= new_snake_x < n and 0<= new_snake_y<n:
                if graph[new_snake_x][new_snake_y] == 1:
                    graph[new_snake_x][new_snake_y] = 0
                    snake.appendleft((head_x,head_y))                    
                    snake.appendleft((new_snake_x,new_snake_y))
                else:
                    snake.appendleft((head_x,head_y))
                    snake.appendleft((new_snake_x,new_snake_y))
                    snake.pop()
            else:
                print(answer)
                exit()
        elif s_dir == 'W':
            head_x, head_y = snake.popleft()
            new_snake_x,new_snake_y = head_x, head_y-1
            answer+= 1
            if (new_snake_x,new_snake_y) in snake:
                print(answer)
                exit()
            if 0 <= new_snake_x < n and 0<= new_snake_y<n:
                if graph[new_snake_x][new_snake_y] == 1:
                    graph[new_snake_x][new_snake_y] = 0
                    snake.appendleft((head_x,head_y))                    
                    snake.appendleft((new_snake_x,new_snake_y))

                else:
                    snake.appendleft((head_x,head_y))
                    snake.appendleft((new_snake_x,new_snake_y))
                    snake.pop()
            else:
                print(answer)
                exit()
        elif s_dir == 'S':
            head_x, head_y = snake.popleft()
            new_snake_x,new_snake_y = head_x+1, head_y
            answer+= 1
            if (new_snake_x,new_snake_y) in snake:
                print(answer)
                exit()
            if 0 <= new_snake_x < n and 0<= new_snake_y<n:
                if graph[new_snake_x][new_snake_y] == 1:
                    graph[new_snake_x][new_snake_y] = 0
                    snake.appendleft((head_x,head_y))                    
                    snake.appendleft((new_snake_x,new_snake_y))
                else:
                    snake.appendleft((head_x,head_y))
                    snake.appendleft((new_snake_x,new_snake_y))
                    snake.pop()
            else:
                print(answer)
                exit()
    if command[1] == 'L':
        if s_dir == 'E':
            s_dir = 'N'
        elif s_dir == 'N':
            s_dir = 'W'
        elif s_dir == 'W':
            s_dir = 'S'
        elif s_dir == 'S':
            s_dir = 'E'

    elif command[1] == 'D':
        if s_dir == 'E':
            s_dir = 'S'
        elif s_dir == 'N':
            s_dir = 'E'
        elif s_dir == 'W':
            s_dir = 'N'
        elif s_dir == 'S':
            s_dir = 'W'
      
while True:
    if s_dir == 'E':
        head_x, head_y = snake.popleft()
        new_snake_x,new_snake_y = head_x, head_y+1
        answer += 1
        if (new_snake_x,new_snake_y) in snake:
            print(answer)
            exit()
        if 0 <= new_snake_x < n and 0 <= new_snake_y < n:
            if graph[new_snake_x][new_snake_y] == 1:
                graph[new_snake_x][new_snake_y] = 0
                snake.appendleft((head_x,head_y))                    
                snake.appendleft((new_snake_x,new_snake_y))
            else:
                snake.appendleft((head_x,head_y))
                snake.appendleft((new_snake_x,new_snake_y))
                snake.pop()
        else:
            print(answer)
            exit()
    elif s_dir == 'N':
        head_x, head_y = snake.popleft()
        new_snake_x,new_snake_y = head_x-1, head_y
        answer+= 1
        if (new_snake_x,new_snake_y) in snake:
            print(answer)
            exit()
        if 0 <= new_snake_x < n and 0<= new_snake_y<n:
            if graph[new_snake_x][new_snake_y] == 1:
                graph[new_snake_x][new_snake_y] = 0
                snake.appendleft((head_x,head_y))                    
                snake.appendleft((new_snake_x,new_snake_y))
            else:
                snake.appendleft((head_x,head_y))
                snake.appendleft((new_snake_x,new_snake_y))
                snake.pop()
        else:
            print(answer)
            exit()
    elif s_dir == 'W':
        head_x, head_y = snake.popleft()
        new_snake_x,new_snake_y = head_x, head_y-1
        answer+= 1
        if (new_snake_x,new_snake_y) in snake:
            print(answer)
            exit()
        if 0 <= new_snake_x < n and 0<= new_snake_y<n:
            if graph[new_snake_x][new_snake_y] == 1:
                graph[new_snake_x][new_snake_y] = 0
                snake.appendleft((head_x,head_y))                    
                snake.appendleft((new_snake_x,new_snake_y))

            else:
                snake.appendleft((head_x,head_y))
                snake.appendleft((new_snake_x,new_snake_y))
                snake.pop()
        else:
            print(answer)
            exit()
    elif s_dir == 'S':
        head_x, head_y = snake.popleft()
        new_snake_x,new_snake_y = head_x+1, head_y
        answer+= 1
        if (new_snake_x,new_snake_y) in snake:
            print(answer)
            exit()
        if 0 <= new_snake_x < n and 0<= new_snake_y<n:
            if graph[new_snake_x][new_snake_y] == 1:
                graph[new_snake_x][new_snake_y] = 0
                snake.appendleft((head_x,head_y))                    
                snake.appendleft((new_snake_x,new_snake_y))
            else:
                snake.appendleft((head_x,head_y))
                snake.appendleft((new_snake_x,new_snake_y))
                snake.pop()
        else:
            print(answer)
            exit()
    
