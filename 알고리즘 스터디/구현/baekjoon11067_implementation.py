# import sys

# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     cafe = []

#     for _ in range(n):
#         cafe.append(list(map(int,input().split())))
#     cafe.sort(key= lambda x : (x[0]))
    
    
#     cafe_list=list(map(int,input().split()))

#     answer = []
#     answer.append(cafe[0])
#     cafe.pop(0)
    
#     direction = 0 # 0은 동, 1은 북, 2는 남
#     if cafe[1][1] == 0:
#         direction = 0
#     elif cafe[1][1] < 0:
#         direction = 2
#     else:
#         direction = 1
    
#     tmp=[]
#     while True:
#         if len(answer) == n:
#             break
#         if tmp:
#             tmp.sort(key=lambda x : x[1])
#             cy = answer[-1][1]
#             if cy > tmp[-1][1]:
#                 direction = 2
#                 answer.extend(tmp)
#                 tmp = []
#             else:
#                 direction = 1
#                 answer.extend(tmp)
#                 tmp =[]
#         px,py = answer[-1]
        
#         if direction == 0:            
#             for i in range(len(cafe)):
#                 dx,dy = cafe[i]
#                 if px == dx:
#                     tmp.append(cafe[i])
#                     cafe.pop(i)
#                     break
#                 if px < dx and py == dy:
#                     answer.append(cafe[i])
#                     cafe.pop(i)
#                     break
#                 else:
#                     continue
        
#         if direction == 1:
#             cafe.sort(key=lambda x : (x[0],x[1]))
#             for i in range(len(cafe)):
#                 dx,dy = cafe[i]
#                 if px == dx:
#                     if py < dy:
#                         answer.append(cafe[i])
#                         cafe.pop(i)
#                         break
#                 if px < dx:
#                     if py < dy:
#                         answer.append(cafe[i])
#                         cafe.pop(i)
#                         direction = 0
#                         break
                    
                
#         if direction == 2:
#             cafe.sort(key= lambda x : (x[0],-x[-1]))
#             for i in range(len(cafe)):
#                 dx,dy = cafe[i]
#                 if px == dx:
#                     if py > dy:
#                         answer.append(cafe[i])
#                         cafe.pop(i)
#                         break
                    
#                 if px < dx:
#                     if py > dy:
#                         answer.append(cafe[i])
#                         cafe.pop(i)
#                         direction = 0
#                         break
                  
                
#     cafe_list.pop(0)  
#     for i in cafe_list:
#         print(answer[i-1])
#     print(answer)
    
    
    
        
#     # for i in range(n-1):
#     #     px,py = answer[i]
        
        
        
        
        
        
#     #     if direction == 0:    
#     #         for j in range(i+1,n):
#     #             dx,dy = cafe[j]
#     #             if py == dy and px < dx:
#     #                 answer.append(cafe[j])
#     #             if cx == dx and dy != py:
#     #                 if dy < py:
#     #                     direction = 1
#     #                 else:
#     #                     direction = 2
            
            



import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cafe = list(tuple(map(int,input().split())) for _ in range(n))        
    cafe.sort()
    
    
    
    answer = [(-1,0)]
 
    tmp = [(-1,0)]
    px,py = (-1,0)
    i = 0
    while i < n:
        if px == cafe[i][0]:
            tmp.append(cafe[i])

        else:
            if answer[-1][1] != tmp[0][1]:
                tmp.reverse()

            answer.extend(tmp)
            tmp = [cafe[i]]
            px,py = cafe[i]
        i += 1
    if tmp[0] not in answer:
        if answer[-1][1] != tmp[0][1]:
            tmp.sort(reverse=True)
        answer.extend(tmp)
        
    cafe_list=list(map(int,input().split()))

    for i in range(1, len(cafe_list)):
        print(*answer[cafe_list[i] + 1])
    
    
    
    
