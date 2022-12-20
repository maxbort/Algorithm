n, m, h = map(int, input().split())

root_list = []
for i in range(m):
    root_list.append(list(map(int,input().split())))

root_list.sort(key=lambda x: (x[0],x[1]))


point = 1
check = 1
answer = []
while True:
    point = 1
    for s,e in root_list:
        if e == point:
            point += 1
        elif e - 1 == point:
            point -= 1
    
    answer.append(point)
    break
    
print(answer)