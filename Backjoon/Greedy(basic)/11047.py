n ,k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

c = 0
p = 0
for i in reversed(range(n)):
    p = k//coin[i]
    c += p 
    k -= coin[i]*p
        
print(c)