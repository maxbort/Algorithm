import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print(0)    
        else:
            print(heappop(heap))
    else:
        heappush(heap, a)

