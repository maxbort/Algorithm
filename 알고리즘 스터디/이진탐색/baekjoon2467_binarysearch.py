import sys
input = sys.stdin.readline

n = int(input())
liq = list(map(int,input().split()))

answer = 1000000000000
ans1 = 0
ans2 = 0

for i in range(n-1):
    check = liq[i]
    start = i+1
    end = n-1
    
    while start <= end:
        mid = (start+end)//2
        temp = check + liq[mid]

        if abs(temp) < answer:
            answer = abs(temp)
            ans1 = i
            ans2 = mid
            
            if temp == 0:
                break
            
        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
            
print(liq[ans1], liq[ans2])