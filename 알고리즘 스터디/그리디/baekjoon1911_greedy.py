import sys

input = sys.stdin.readline

n,l = map(int,input().split())

road = [list(map(int,input().split())) for _ in range(n)]

road.sort(key=lambda x : (x[0],x[1]))

rest_len = 0
cnt = 0
tmp = 0
for i in road:
    if tmp >= i[0]:
        rest_len = i[1] - tmp
    else:
        rest_len = i[1]-i[0]
        tmp = i[0]
    

    while rest_len > 0:
        if rest_len >= l:
            rest_len -= l
            cnt += 1
        else:
            rest_len -= l
            cnt += 1
            tmp = i[1] - rest_len
            break
        
print(cnt)