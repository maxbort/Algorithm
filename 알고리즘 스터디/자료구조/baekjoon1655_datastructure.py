import sys
import heapq

input = sys.stdin.readline

n = int(input())

min_heap = []
max_heap = []

for _ in range(n):
    num = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(min_heap, -num)
    else:
        heapq.heappush(max_heap, num)

    print(min_heap, "min_h")
    print(max_heap, " max_h")
    if max_heap and max_heap[0] < -min_heap[0]:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(max_heap)

        heapq.heappush(min_heap, -b)
        heapq.heappush(max_heap, -a)
    
    print(-min_heap[0])
