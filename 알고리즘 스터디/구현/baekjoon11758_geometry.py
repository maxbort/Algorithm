import sys
input = sys.stdin.readline

dot = [list(map(int,input().split())) for _ in range(3)]

p1,p2,p3 = dot

def ccw(p1,p2,p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1]))

if ccw(p1,p2,p3) >0:
    print(1)
elif ccw(p1,p2,p3) < 0:
    print(-1)
else:
    print(0)
