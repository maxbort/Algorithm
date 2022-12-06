import heapq

n, k = map(int,input().split())
jew = []
for _ in range(n):
    heapq.heappush(jew, list(map(int,input().split())))

C=[]
for _  in range(k):
    C.append(int(input()))

C.sort()
temp = []
answer = 0

for i in C:
    while jew and i >= jew[0][0]:
        heapq.heappush(temp, -heapq.heappop(jew)[1])
    if temp:
        answer -= heapq.heappop(temp)
    elif not jew:
        break

print(answer)