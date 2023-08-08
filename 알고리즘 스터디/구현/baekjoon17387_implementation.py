# 시간 초과로 틀린 코드

# import sys
# from fractions import Fraction
# input = sys.stdin.readline

# line1 = list(map(int,input().split()))
# line2 = list(map(int,input().split()))

# 선분 교차를 수식으로 증명.
# 방정식으로 증명은 시간초과 날듯
# lx1, ly1, lx2, ly2 = line1
# inc = Fraction((lx1-lx2), (ly1-ly2))

# 1. 방향벡터 확인
# 1-2 평행일 시 겹치는 지 확인 후 안겹치면 안만나는 걸로
# 2. 두 선분의 직선의 방정식을 구함
# 2-2. 각 선분을 연장한 직선들끼리 봤을 때 line1의 방정식이 f1, line2의 방정식이 f2라고 하였을때,
# f1이 line2와 만나고 f2가 line1과 만난다면 line1과 line2는 만난다.
# 2-3. 만나는 것의 조건 판별은? f1이 line2와 만난다고 하였을 때, line2의 각 끝점을 f1에 대입했을 때, f1을 기준으로 
# 두 점이 위아래로 나뉜다. 즉, 대입 했을 때 두 값을 곱했을 때 음수값이 나오거나 0이 되면(한점이 접할때) 된다.
# 2-4. 그 f1이라는 직선을 수직선에서의 x축으로 생각하면 하면 이해가 편함.
# 생각해보니 이렇게 하면 방향벡터 구할 필요가 없음

# import sys
# from fractions import Fraction
# input = sys.stdin.readline

# line1 = list(map(int,input().split()))
# line2 = list(map(int,input().split()))

# def check_line(line1,line2):
#     x1,y1,x2,y2 = line1
#     x3,y3,x4,y4 = line2
    
#     m = Fraction((y1-y2),(x1-x2))
#     f1 = (y3-y1) - m*(x3-x1)
#     f2 = (y4-y1) - m*(x4-x1)
    
#     if f1*f2 >0:
#         return False
#     else:
#         return True
    
# def check_final():
#     a = check_line(line1,line2)
#     b = check_line(line2,line1)
    
#     if a and b:
#         return 1
#     else:
#         return 0
    
# print(check_final())

# # 맞지만 시간 초과;

import sys
from fractions import Fraction
input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

check1 = ccw(x1,y1,x2,y2,x3,y3)* ccw(x1,y1,x2,y2,x4,y4)
check2 = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)

if check1 == 0 and check2 ==0 :
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        print(1)
        exit()

else:
    if check1 <= 0 and check2 <= 0:
        print(1)
        exit()
print(0)