import sys
input = sys.stdin.readline

n = int(input())
alpha = []
value = {}

for _ in range(n):
    alpha.append(list(input().rstrip()))

for alphabet in alpha:
    for i in range(len(alphabet)):
        if alphabet[i] not in value:
            value[alphabet[i]] = 10 ** (len(alphabet) - 1 - i)
        else:
            value[alphabet[i]] += 10 ** (len(alphabet) - 1 - i)
            
value = sorted(value.items(), key=lambda x : x[1], reverse=True)

alpha_to_num = {}

num = 9

for i in value:
    alpha_to_num[i[0]] = num
    num -= 1
answer = 0

for j in alpha:
    num = ""
    for alphabet in j:
        num += str(alpha_to_num[alphabet])
    
    answer += int(num)
    
print(answer)