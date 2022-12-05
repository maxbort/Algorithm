n = int(input())

bd = []

for i in range(n):
    bd.append(list(map(int,input().split())))
result = []

for i in range(len(bd)):
    tot = 0
    for j in range(len(bd[i])):
        if j == 0:
            tot += bd[i][0]
            result.append(tot)
        if bd[i][j] == -1:
            break
        elif j==1 and bd[i][j] != -1:
            num = bd[i][j] -1
            if len(result) > num:
                tot += result[num]
                result[i] = tot

for i in result:
    print(i)            
