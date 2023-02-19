import sys
input = sys.stdin.readline

n = int(input())

cnt = [0] * 30001

for i in range(2, n+1):
    cnt[i] = cnt[i-1] + 1
    
    if i % 5 == 0:
        cnt[i] = min(cnt[i],cnt[i//5]+1)
    if i % 3 == 0:
        cnt[i] = min(cnt[i],cnt[i//3]+1)
    if i % 2 == 0:
        cnt[i] = min(cnt[i],cnt[i//2]+1)
    
print(cnt[n])