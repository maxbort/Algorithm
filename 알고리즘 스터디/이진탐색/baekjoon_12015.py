n = int(input())
num = list(map(int,input().split()))

seq = [0]

for check in num:
    if seq[-1] < check:
        seq.append(check)
    else:
        s = 0
        e = len(seq)

        while s < e:
            mid = (s+e) // 2

            if seq[mid] < check:
                s = mid + 1
            else:
                e = mid
            
        seq[e] = check

print(len(seq) - 1)