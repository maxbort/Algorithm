import sys
input = sys.stdin.readline  

n = int(input())

work = [[] for _ in range(n+1)]
working_time = [0] *(n+1)
for i in range(1,n+1):
    part = list(map(int,input().split()))
    working_time[i] = part[0]
    if part[1] == 0:
        continue
    else:
        for j in part[2:]:
            work[i].append(j)


for i in range(1,n+1):
    a = 0
    for j in work[i]:
            a = max(a, working_time[j])
    working_time[i] += a
        
print(max(working_time))