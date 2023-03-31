import sys
import heapq
input = sys.stdin.readline

n = int(input())

major = []

for _ in range(n):
    major.append(list(map(int,input().split())))

major.sort(key=lambda x : x[0])

room = []
heapq.heappush(room,major[0][1])

for i in range(1,n):
    if major[i][0] < room[0]:
        heapq.heappush(room,major[i][1])
        
    else:
        heapq.heappop(room)
        heapq.heappush(room,major[i][1])

print(len(room))