import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int,input().split()))

answer = [-100000000000000]
dp = [0] * (n+1)
for i in range(1, n+1):
    if answer[-1] < num[i]:
        answer.append(num[i])
        dp[i] = len(answer) - 1
        
    else:
        s = 0
        e = len(answer)
        while s < e:
            mid = (s+e) // 2
            if answer[mid] < num[i]:
                s = mid + 1
            else:
                e = mid
        answer[e] = num[i]
     
max_idx,ans = max(dp)+1,[]
for i in range(n,0,-1):
    if dp[i] == max_idx-1:
        ans.append(num[i])
        max_idx = dp[i]

print(len(answer) - 1)
print(*ans[::-1],sep=' ')



import bisect as bs

n = int(input())
nums = [0] + list(map(int,input().split()))
dp = [0]*(n+1)

cp = [-float('inf')]

for i in range(1, n+1):
    if nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp)-1
    else:
        dp[i] = bs.bisect_left(cp,nums[i])
        cp[dp[i]] = nums[i]
print(len(cp)-1)
            
# 역추적
max_idx,ans = max(dp)+1,[]
for i in range(n,0,-1):
    if dp[i] == max_idx-1:
        ans.append(nums[i])
        max_idx = dp[i]
print(*ans[::-1])