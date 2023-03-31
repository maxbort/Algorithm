import sys

input = sys.stdin.readline

n = int(input())
weight_list = list(map(int,input().split()))

weight_list.sort()

checkpoint = 0 
for i in weight_list:
    if checkpoint == 0:
        if i > 1:
            break
        else:
            checkpoint = i
    else:
        if checkpoint + 1 >= i:
            checkpoint += i
        else:
            break
        
answer = checkpoint+1

print(answer)