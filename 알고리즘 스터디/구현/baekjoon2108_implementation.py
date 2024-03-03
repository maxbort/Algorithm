import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

num.sort()

num_counts = Counter(num)
common = num_counts.most_common()
    

print("===============================")
print(round(sum(num)/n))
print(num[n//2])
if len(common) > 1 and common[0][1] == common[1][1]:
    print(print(common[1][0]))
else:
    print(common[0][0])
print(abs(max(num) - min(num)))