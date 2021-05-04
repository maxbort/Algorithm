a,m,d,n = input().split()

a= int(a)
m = int(m)
n = int(n)
d = int(d)
i = 1
while i < n:
    a = a*m+d
    i+=1


print(a)
