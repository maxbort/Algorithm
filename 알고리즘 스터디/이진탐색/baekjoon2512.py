import sys
input = sys.stdin.readline

n = int(input())
city = list(map(int,input().split()))
total_money = int(input())

city.sort()
start = 0
end = max(city)

while start <= end:
    mid = (start+end) // 2
    check = 0
    for i in city:
        if i > mid:
            check += mid
        else:
            check += i
    if check <= total_money:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)