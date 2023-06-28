import sys
input = sys.stdin.readline
n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

dp = []

for i in range(n):
    if i == 0 :
        dp.append(a[i])
    elif i == 1:
        dp.append(dp[0] + a[i])
    elif i == 2:
        dp.append(max(dp[1], a[i] + a[i-1], a[0] + a[i]))
    else:
        dp.append(max(dp[i-1], dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i]))
        
print(max(dp))
        