
# import sys
# from collections import deque
# input = sys.stdin.readline

# n,w,l = map(int,input().split())
# # n은 트럭수, w는 다리길이, l은 최대하중
# bus = deque((map(int,input().split())))
# on_bridge = deque([0 for _ in range(w)])
# answer = 0


# while bus:
#     on_bridge.popleft()
#     if len(on_bridge) < w:
#         if sum(on_bridge) + bus[0] <= l:
#             on_bridge.append(bus.popleft())
#         else:
#             on_bridge.append(0)
#     answer += 1
# answer += w
# print(answer)



import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
bus = deque((map(int, input().split())))
on_bridge = deque()
answer = 0

while True:
    if len(on_bridge) == w:
        on_bridge.popleft()
    if on_bridge and sum(on_bridge) + bus[0] > l:
        on_bridge.append(0)
    else:
        if bus:
            on_bridge.append(bus.popleft())

    answer += 1
    if not bus:
        break
answer += w
print(answer)
