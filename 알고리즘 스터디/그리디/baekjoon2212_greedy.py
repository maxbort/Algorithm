import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

sensor = list(map(int,input().split()))
sensor.sort()
dist = []

for i in range(n-1):
    dist.append(sensor[i+1] - sensor[i])

dist.sort()
answer= 0
for j in range(n-k):
    answer+=dist[j]
    
print(answer)

