# import sys
# from itertools import combinations

# input = sys.stdin.readline

# n, m = map(int, input().split())
# city = list(list(map(int, input().split())) for _ in range(n))
# result = 999999
# house = []      # 집의 좌표
# chick = []      # 치킨집의 좌표

# for i in range(n):
#     for j in range(n):
#         if city[i][j] == 1:
#             house.append([i, j])
#         elif city[i][j] == 2:
#             chick.append([i, j])

# for chi in combinations(chick, m):  # m개의 치킨집 선택
#     temp = 0            # 도시의 치킨 거리
#     for h in house: 
#         chi_len = 999   # 각 집마다 치킨 거리
#         for j in range(m):
#             chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
#         temp += chi_len
#     result = min(result, temp)

# print(result)




import sys
from itertools import combinations
input = sys.stdin.readline

INF = float("inf")
n,m = map(int,input().split())

graph = [] 
home = []  
chicken = []  
for _ in range(n):
    graph.append(list(map(int,input().split())))  

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i,j]) 
        elif graph[i][j] == 2:
            chicken.append([i,j])  

result = INF  # 결과를 저장할 변수, 초기값은 무한대로 설정
for c in combinations(chicken, m):  # 치킨집 리스트에서 m개를 선택하는 모든 조합에 대해 반복
    tmp = 0  
    for h in home:  
        length = 9999  
        for j in range(m):
            length = min(length, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))  # 현재 집과 선택한 치킨집 사이의 거리 계산
        tmp += length  # 현재 집의 치킨 거리를 누적
    result = min(result, tmp)  # 현재 조합과 전 결과 비교하여 최솟값 갱신
    
print(result)



# cnt = [[0,i] for i in range(len(chicken))]


# for i in range(len(home)):
#     hx,hy = home[i][0], home[i][1]
#     tmp = INF
#     a = 0
#     for j in range(len(chicken)):
#         cx,cy = chicken[j][0],chicken[j][1]   
#         dist = abs(hx-cx) + abs(hy-cy)
#         if dist < tmp:
#             tmp = dist
#             a = j
#     cnt[a][0] += 1

# cnt.sort()
# print(cnt)
# que = deque(cnt)
# temp = len(chicken)

# while temp > m:
#     a, di = que.popleft()
#     chicken[di] = (-1,-1)
#     temp -= 1

# answer = 0
# for i in range(len(home)):
#     hx,hy = home[i][0], home[i][1]   
#     tmp = INF
#     for j in range(len(chicken)):
#         cx,cy = chicken[j][0],chicken[j][1]
#         if cx != -1 and cy != -1:
#             dist = abs(hx-cx) + abs(hy-cy)
#             if dist <= tmp:
#                 tmp = dist
#     answer += tmp
    
# print(answer)