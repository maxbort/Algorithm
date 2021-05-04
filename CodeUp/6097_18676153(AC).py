k = []
h,w = input().split()
h = int(h)
w = int(w)
for i in range(h):
    k.append([])
    for j in range(w):
        k[i].append(0)
n = int(input())
for i in range(n):
    l,d,x,y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    for j in range(l):
        if d == 0:
            k[x-1][y-1] = 1
            y += 1
        else:
            k[x-1][y-1] = 1
            x += 1


for i in range(h):
    for j in range(w):
        print(k[i][j], end=' ')
    print()


