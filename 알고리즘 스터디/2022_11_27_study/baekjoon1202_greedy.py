import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().split())

jew = []
for i in range(n):
    weight, price = map(int,input().split())
    jew.append([weight,price])

bags= []
for i in range(k):
    bags.append(int(input()))

jew.sort(key=lambda x: (x[1], -x[0]), reverse=True)
bags.sort()

result = 0
for i in jew:
    for j in range(len(bags)):
        if i[0] < bags[j]:
            result += i[1]
            bags[j] = 0
            continue
        
        
print(result)

