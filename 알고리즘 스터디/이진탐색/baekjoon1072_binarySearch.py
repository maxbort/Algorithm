import sys
input = sys.stdin.readline
 
 
X, Y = map(int, input().split())
Z = (Y * 100) // X
if Z >= 99:
    print(-1)
else:
    answer = 0
    s = 1
    e = X
 
    while s <= e:
        mid = (s + e) // 2
        if (Y+mid)*100 // (X+mid) <= Z:
            s = mid+1
        else:
            answer = mid
            e = mid - 1
 
    print(answer)