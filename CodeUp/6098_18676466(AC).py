a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
a=[list(map(int, input().split())) for __ in range(10)]

x, y = 1, 1

while True:
    if a[x][y] == 2:
        a[x][y] = 9
        break
    elif (a[x][y+1]) == 1:
        if a[x+1][y] == 1:
            a[x][y] = 9
            break
        else:
            a[x][y] = 9
            x +=1
    else:
        a[x][y] = 9
        y += 1
for i in range(10):
    for j in range(10):
        print(int(a[i][j]), end=' ')
    print()
