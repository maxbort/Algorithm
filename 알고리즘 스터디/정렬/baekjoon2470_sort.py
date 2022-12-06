n = int(input())

liquid = list(map(int,input().split()))

liquid.sort()

l, r = 0, n-1
flag = abs(liquid[l] + liquid[r])
answer = []
while l < r:
    result = liquid[l] + liquid[r]
    if abs(result) < flag:
        flag = abs(result)
        answer = [l,r]
        if flag == 0:
            break
    if result > 0:
        r = r - 1
    else:
        l += 1
                

print(liquid[answer[0]], liquid[answer[1]])
            