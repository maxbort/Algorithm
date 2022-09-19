coin = [500,100,50,10]

n = int(input())

total = 0
for i in range(4):
    total += int(n/coin[i])
    n = int(n%coin[i])
print(total)