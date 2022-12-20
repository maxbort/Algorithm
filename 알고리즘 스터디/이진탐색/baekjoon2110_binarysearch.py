import math

n,c = map(int,input().split())

home = []

for i in range(n):
    home.append(int(input()))

home.sort()

start = 1
end = home[-1] - home[0]
result = end
        
if c < 3:
    print(result)
else:
    while start <= end:
        mid = (start+end) // 2
        point = home[0]
        cnt = 1
        
        for i in range(1,len(home)):
            if abs(home[i] - point) >= mid:
                cnt += 1
                point = home[i]
        if cnt >= c:
            result = mid
            start = mid + 1
        elif cnt < c:
            end = mid - 1
    print(result)