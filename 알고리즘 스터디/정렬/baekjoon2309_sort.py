list = []
answer = []
sum = 0
for i in range(9):
    n = int(input())
    sum += n
    list.append(n)
list.sort()
i = 8
j = 0
while(True):
    tmp = sum - list[i] - list[j]
    if tmp >100:
        j+=1
    if tmp <100:
        i -=1
    if tmp == 100:
        break
list.pop(i)
list.pop(j)
for i in range(7):
    print(list[i])
