import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 10
d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3,n+1):
    d[i] = (d[i-2]*2 + d[i-1]) % 796796

print(d)
print(d[n])