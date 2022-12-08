n, k = map(int,input().split())

list = []
for i in range(n):
    list.append(int(input()))

list.sort()
start = 1
end = max(list)
answer = 0

while start <= end:
    temp= 0
    mid = (start + end) // 2
    for i in list:
        if i >= mid:
            temp += ( i//mid )
    if temp >= k:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
            
print(answer)