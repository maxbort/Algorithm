import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
num_list_rev = num_list[::-1]

increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            increase[i] = max(increase[i],increase[j]+1)


for i in range(n):
    for j in range(i):
        if num_list_rev[i] > num_list_rev[j]:
            decrease[i] = max(decrease[i],decrease[j]+1)

answer = [0 for _ in range(n)]

for a in range(n):
    answer[a] = increase[a]+decrease[(n-a-1)]-1
    
print(max(answer))


