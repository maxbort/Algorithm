import sys
from collections import deque

cnt1,cnt2 = 0,0

num = list(map(int,input()))
q = deque()
q2 = deque()
for i in range(len(num)):
    if num[i] == 0:
        q.append(num[i])
    else:
        if q:
            cnt1 += 1
            q = deque()
            
for i in range(len(num)):
    if num[i] == 1:
        q2.append(num[i])
    else:
        if q2:
            cnt2 += 1
            q2 = deque()

if q:
    cnt1+=1
if q2:
    cnt2 += 1

print(min(cnt1,cnt2))
            
