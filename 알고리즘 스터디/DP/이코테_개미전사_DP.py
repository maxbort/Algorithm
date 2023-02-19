import sys
input = sys.stdin.readline

n = int(input())
food_storage = list(map(int,input().split()))

d = [0] * 100

d[0] = food_storage[0]
d[1] = max(food_storage[0],food_storage[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + food_storage[i])


print(max(d))