import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 31


dp[2] = 3

for i in range(4,n+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2])*2 + 2

if n % 2 == 1:
    print(0)
else:
    print(dp[n])