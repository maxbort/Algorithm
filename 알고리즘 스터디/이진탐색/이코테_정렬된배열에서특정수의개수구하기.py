import sys
import time

start_time = time.time()
input = sys.stdin.readline

n, m = map(int,input().split())

num_list = list(map(int,input().rstrip().split()))

def first_idx(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        return first_idx(arr,start, mid -1, target)
    else:
        return first_idx(arr,mid + 1, end, target)
             
             
def last_idx(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if (mid == n-1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last_idx(arr,start, mid -1, target)
    else:
        return last_idx(arr,mid + 1, end, target)
    
first = first_idx(num_list, 0, n-1, m)
last = last_idx(num_list,0, n-1, m)
if first == None:
    first = 0
result = last - first + 1

if result == 0:
    print(-1)
else:
    print(result)
    
end_time = time.time()
print(f"걸린 시간 : {end_time - start_time}")