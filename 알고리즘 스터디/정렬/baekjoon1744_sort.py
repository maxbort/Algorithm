from collections import deque

n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))


sort_num = deque(sorted(num, reverse=True))


answer = 0

while sort_num:
    if len(sort_num) == 1:
        answer += sort_num.popleft()
        break
    
    x = sort_num.popleft()
    print(x)
    if x > 1:
        y = sort_num.popleft()
        if y > 1:
            answer += x*y
        if y == 1:
            answer += (x + y)
        if y < 1:
            answer += x
            sort_num.appendleft(y)
    if x == 1:
        answer += x
    
    if x == 0:
        if len(sort_num) %2 == 1:
            y = sort_num.popleft()
            answer += x*y
        else:
            answer += x
    
    if x < 0:
        sort_num.appendleft(x)
        x = sort_num.pop()
        y = sort_num.pop()
        answer += x*y

print(answer)
        
        
        
    
    
    
            

                
            
    
         