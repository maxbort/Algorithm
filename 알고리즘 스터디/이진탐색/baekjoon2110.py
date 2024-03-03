import sys

input = sys.stdin.readline

n,m = map(int,input().split())

home = []
for _ in range(n):
    home.append(int(input()))

home.sort()

start = 1
end = home[-1] - home[0]
answer = end

if m < 3:
    print(answer)
else:
    while start <= end:
        mid = (start+end) // 2
        point = home[0]
        cnt = 1
        
        for i in range(1,n):
            if abs(home[i] - point) >= mid:
                cnt += 1
                point = home[i]
        if cnt >= m:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)