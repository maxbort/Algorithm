import sys

input = sys.stdin.readline

n = int(input())
budget = list(map(int,input().split()))
total_budget = int(input())

budget.sort()

if sum(budget) <= total_budget:
    print(max(budget))
else:
    start = 0
    end = n-1
    while True:
        check = sum(budget[:start])
        check2 = (total_budget - check)//(n-start)
        if check2 <= budget[start]:
            break
        else:
            start += 1
    print(check2)