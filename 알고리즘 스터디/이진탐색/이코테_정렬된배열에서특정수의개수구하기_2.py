from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    right_idx = bisect_right(arr, right_value)
    left_idx = bisect_left(arr, left_value)
    return right_idx - left_idx

n, m = map(int,input().split())
arr = list(map(int,input().split()))


cnt = count_by_range(arr, m, m)

if cnt == 0:
    print(-1)
else:
    print(cnt)