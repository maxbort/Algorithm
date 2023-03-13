import sys
input = sys.stdin.readline

n = int(input())

liq = list(map(int,input().split()))

start = 0
end = n - 1

temp = abs(liq[start] + liq[end])
ans1 = 0
ans2 = n-1
while start < end:
    a = liq[start] + liq[end]
    if abs(a) < temp:
        temp = abs(a)
        ans1 = start
        ans2 = end
        if a == 0:
            break
        
    if a < 0:
        start += 1
    else:
        end -= 1
print(liq[ans1], liq[ans2])