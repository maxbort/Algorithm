t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0]*2
    def fibonacci(n,dp):
        if (n == 0):
            dp[0] += 1
            return 0
        elif (n == 1):
            dp[1] += 1
            return 1
        else:
            return fibonacci(n-1,dp) + fibonacci(n-2,dp)
    fibonacci(n,dp)
    print(dp[0],dp[1])
    


