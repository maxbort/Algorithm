import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()

answer = []
check = 4e9
if n == 3:
    num_list.sort()
    print(num_list[0], num_list[1], num_list[2])
for i in range(n-2):
    third = num_list.pop()
    start, end = 0, len(num_list)-1
        
    while start != end:
        temp = num_list[start] + num_list[end] + third
            
        if check >= abs(temp):
            check = abs(temp)
            answer = [num_list[start], num_list[end], third]
                
        if temp < check:
            start += 1
        else:
            end -= 1
        if check == 0 :
            break
answer.sort()
print(answer[0], answer[1],answer[2])