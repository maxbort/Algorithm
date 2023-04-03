# import sys

# input = sys.stdin.readline

# n = int(input())

# times = [0] * (n+1)
# root = [0] * (n+1)
# answer = [0] * (n+1)


# for i in range(n):
#     temp = list(map(int,input().split()))
#     times[i+1] = temp[0]
#     if temp[1:len(temp)-1]:
#         root[i+1] = temp[1:len(temp)-1]
#     else:
#         root[i+1] = [0]
    

# for j in range(1,n+1):
#     tmp = []
#     for construct in root[j]:
#         if construct == 0:
#             answer[j] = times[j]   
#         else:
#             for k in root[construct]:
#                 if k in root[j]:
#                     root[j].remove(k)
#             tmp.append(answer[construct])
#     answer[j] = sum(tmp) + times[j]


# for i in range(1,n+1):
#     print(answer[i])




import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

building = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
times = [0] * (n+1)

for i in range(1,n+1):
    temp = list(map(int,input().split()))
    times[i] = temp[0]
    data = temp[1:len(temp)-1]

    for j in data:
        building[j].append(i)
        indegree[i] += 1


def topology_sort():
    answer = [0] * (n+1)
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        
        answer[now] += times[now]

        for b in building[now]:
            indegree[b] -= 1
            
            answer[b] = max(answer[b], answer[now])

            if indegree[b] == 0:
                q.append(b)
    return answer


answer = topology_sort()

for i in range(1,n+1):
    print(answer[i])