import sys
from collections import deque


input = sys.stdin.readline
symbol = list(input().rstrip())
stack=[]
multy = 1
answer = 0
for i in range(len(symbol)):
    if symbol[i] == "(":
        stack.append(symbol[i])
        multy *= 2
    elif symbol[i] == "[":
        stack.append(symbol[i])
        multy *= 3
        
    elif symbol[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if symbol[i-1] == "(":
            answer += multy
        stack.pop()
        multy //=2
        
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if symbol[i-1] == "[":
            answer += multy
            
        stack.pop()
        multy //= 3
        
if stack:
    print(0)
else:
    print(answer)
    