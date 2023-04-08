import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = list(map(str,input().rstrip()))
    n = int(input())
    if n == 0:
        num = []
        temp = input()
    else:
        num = list(map(int,input().rstrip()[1:-1].split(",")))
        num = deque(num)
    check = 0
    flag = 1
    for i in func:
        if i == 'R':
            check += 1
        elif i == 'D':
            if len(num) == 0:
                print("error")
                flag = 0
                break
            else:
                if check % 2 == 0:
                    num.popleft()
                else:
                    num.pop()
    
    if flag == 0:
        continue
    else:
        if check % 2 == 1:
            num.reverse()
        if num:
            num = list(num)
            print("[",end="")
            print(*num,sep=",",end="")
            print("]")
        else:
            print(list(num))
    
            
