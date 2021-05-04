a = input().split('-')
answer = 0
for i in a[0].split('+'):
    answer += int(i)
for i in a[1:]:
    sum = 0
    for j in i.split('+'):
        sum += int(j)
    answer -= sum
print(answer)
    






