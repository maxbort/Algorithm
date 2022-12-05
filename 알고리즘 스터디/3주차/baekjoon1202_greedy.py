n, k = map(int,input().split())
jew = []
for _ in range(n):
    jew.append(tuple(map(int, input().split())))
jew.sort(key = lambda x: -x[1])
C=[]
for _  in range(k):
    C.append(int(input()))

C.sort(reverse=True)
temp = []
answer = 0

while(C):
    for i in range(n):
        for j in C:
            if jew[i][0] > j:
                continue
            else:
                C.remove(j)
                temp.append(jew[i][1])
                break
answer += sum(temp)
print(answer)


