import sys

input = sys.stdin.readline

n,m = map(int,input().split())
cnt = 1

if n == 1 or m == 1:
    cnt = 1
elif n == 2:
    if m > 6:
        cnt = 4
    elif 5 <= m <= 6:
        cnt = 3
    elif 3<= m <5:
        cnt = 2
    else:
        cnt = 1
elif n > 2:
    if m > 7:
        cnt = 5
        m -= 7
        cnt += m
    elif m == 7:
        cnt = 5
    elif 4<= m < 7:
        cnt = 4
    else:
        cnt += m-1

print(cnt)


