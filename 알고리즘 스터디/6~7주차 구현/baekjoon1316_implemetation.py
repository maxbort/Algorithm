n = int(input())
cnt = 0
for _ in range(n):
    test = input()
    length = len(test)
    tmparray = []
    alpha = 0
    if length == 1:
        cnt+= 1
    else:
        for j in range(length):
            tmp = test[j]
            if j < length-1:
                if test[j] != test[j+1]:
                    tmparray.append(tmp)
                    if j+1 == length:
                        tmparray.append(test[j+1])
            else:
                tmparray.append(test[j])
        for j in tmparray:
            if tmparray.count(j) >1 :
                alpha += 1
        if alpha == 0:
            cnt +=1

    

print(cnt)

