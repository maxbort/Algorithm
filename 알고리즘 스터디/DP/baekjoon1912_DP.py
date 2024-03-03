import sys

input = sys.stdin.readline

n = int(input())
dp = []
num = list(map(int,input().split()))
num.append(0)

for i in range(n):
    dp.append(num[i])
    if num[i] > 0:
        tot = 0
        for j in range(i,n):
            tot += num[j]
            if tot + num[j+1] <= 0:
                dp.append(tot)
                break
            else:
                dp.append(tot)
                continue
    else:
        continue 
print(max(dp))

############# 아래 모범답안

n = int(input())  # 배열의 크기 입력
num = list(map(int, input().split()))  # 배열 입력

# 카데인 알고리즘을 사용하여 최대 부분 배열 합을 찾습니다.
current_max = global_max = num[0]
for i in range(1, n):
    current_max = max(num[i], current_max + num[i])
    global_max = max(global_max, current_max)

print(global_max)
