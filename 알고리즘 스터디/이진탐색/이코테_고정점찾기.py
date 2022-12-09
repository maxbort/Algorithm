import time
import sys
input = sys.stdin.readline


# start_time = time.time()

n = int(input())
# 리스트는 오름차순으로 정렬되어 입력됨
num_list = list(map(int,input().rstrip().split()))

start = 0
end = n-1
answer = 0
while start <= end:
    mid = (start + end) // 2

    if num_list[mid] == mid:
        answer = mid
        break
    elif num_list[mid] < mid:
        start = mid + 1
    elif num_list[mid] > mid:
        end = mid - 1
        
if answer == 0:
    print(-1)
else:
    print(answer)

# end_time = time.time()
# result = end_time - start_time
# print(f'걸린시간 : {result}')



