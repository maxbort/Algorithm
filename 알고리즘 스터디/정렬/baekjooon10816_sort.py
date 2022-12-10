import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
m = int(input())
check_list = list(map(int,input().split()))

answer_list = [0] * m


def find_num(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr,left)
    return right_idx - left_idx


for i in range(m): 
    answer_list[i] = find_num(num_list,check_list[i], check_list[i])

for i in answer_list:
    print(i, end= ' ')