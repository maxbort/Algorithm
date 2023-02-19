import sys
input = sys.stdin.readline

t = int(input())

def renew(a):
    if root[a] == a:
        return a
    else:
        temp = renew(root[a])
        dist[a] += dist[root[a]]
        root[a] = temp
        return temp
    
for i in range(t):
    n = int(input())
    dist = [0] * (n+1)
    root = [i for i in range(n+1)]

    while True:
        order = input().split()
        if order[0] == 'E':
            renew(int(order[1]))
            print(dist,"here is first")
            print(order,"here is first")
            print(dist[int(order[1])])
        elif order[0] == 'I':
            dist[int(order[1])] = abs(int(order[2]) - (int(order[1]))) % 1000
            root[int(order[1])] = int(order[2]) 
            print(dist ,"here is second")
            print(order, "here is second")
        else:
            break

