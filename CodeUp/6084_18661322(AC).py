h,b,c,s = input().split()
h =float(h)
b = float(b)
c = float(c)
s = float(s)

a =float(h*b*c*s)
n = a/8/1024/1024
print(format(n,".1f")+" MB")


