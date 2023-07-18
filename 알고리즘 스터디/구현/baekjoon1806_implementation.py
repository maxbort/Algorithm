import sys
input = sys.stdin.readline

n,s = map(int,input().split())

num = list(map(int,input().split()))

answer = float('INF')

tmp = sum(num)
if tmp < s:
    print(0)
else:
    
    i = 0
    j = n-1
    while i < j:
        if num[i] >= s or num[j] >= s:
            answer = 1
            break
        
        if num[i] >= num[j]:
            temp = tmp - num[j]
            if temp >= s:
                tmp = temp
                j-=1
                answer = min(answer,j - i +1)
            else:
                break
        else:
            temp = tmp - num[i]
            if temp >= s:
                tmp = tmp
                i += 1
                answer = min(answer, j-i+1)
            else:
                break
    if answer == float('inf'):
        print(0)
    else:
        print(answer)