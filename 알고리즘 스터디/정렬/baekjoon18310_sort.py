import sys
input = sys.stdin.readline
n = int(input())
home = list(map(int,input().split()))

result = 100000
point = 100000
for i in home:
    temp = 0
    for j in home:
        temp += (abs(j-i))
    if result >= temp:
        result = temp
        if point >= i:
            point = i

print(point)
