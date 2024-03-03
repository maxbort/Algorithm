import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

first = []
for i in range(n):
    first.append(i+1)

num = 0
answer = []
while first:
    if len(first) == 1:
        answer.append(str(first[0]))
        break
    num += k-1
    if num < len(first):
        answer.append(str(first.pop(num)))
    else:
        num = num%len(first)
        answer.append(str(first.pop(num)))
        
print("<",", ".join(answer)[:],">", sep='')
