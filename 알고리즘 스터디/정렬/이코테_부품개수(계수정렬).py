n = int(input())
A = list(map(int,input().split()))
A.sort()

m = int(input())
B = list(map(int,input().split()))

list = [0] * (max(A) + 1)

for i in A:
    list[i] += 1

for j in B:
    if list[j] != 0:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')