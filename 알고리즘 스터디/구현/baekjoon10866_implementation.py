import sys
from collections import deque
input = sys.stdin.readline

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

q = deque()
n = int(input())

for _ in range(n):
    command = input().rstrip()
    print(command, "here is command")
    if ' ' in command:
        a,b = command.split(' ')
    else:
        a = command
        b = ' '
    

    
    if a == 'push_front':
        q.appendleft(int(b))
    if a == 'push_back':
        q.append(int(b))
    if a == 'pop_front':
        if q:
            print(int(q.popleft()))
        else:
            print(-1)
    if a == 'pop_back':
        if q:
            print(int(q.pop()))
        else:
            print(-1)
    if a == 'size':
        print(len(q))
    if a == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    if a == 'front':
        if not q:
            print(-1)
        else:
            print(int(q[0]))
    if a == 'back':
        if not q:
            print(-1)
        else:
            print(int(q[-1]))


        
