import sys
input = sys.stdin.readline

n,l = map(int,input().split())
pipe = list(map(int,input().split()))

pipe.sort()


check = pipe[0]
answer = 1

for i in range(1,n):
    if pipe[i] - check >= l:
        answer += 1
        check = pipe[i]
    else:
        continue
    
print(answer)