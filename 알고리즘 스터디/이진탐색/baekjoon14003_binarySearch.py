import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

min_num = -float('inf')
dp = [min_num]

answer = 0
answer_list = []
for i in range(len(num_list)):
    for j in range(i-1,len(num_list)):
        if dp[-1] < num_list[j]:
            dp.append(num_list[j])
        else:
            start = 0
            end = len(dp)
            while start < end:
                
                mid = (start+end) // 2
                
                if dp[mid] < num_list[j]:
                    start = mid + 1
                else:
                    end = mid
    print(len(dp))
    if len(dp) > answer:
        answer = len(dp)
        answer_list = dp[1:]
        dp = [min_num]
    else:
        dp = [min_num]

dp.pop(0)
print(answer-1)
print(*answer_list)

# 6
# 10 20 10 30 20 50