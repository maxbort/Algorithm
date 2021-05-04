n = int(input())

conf = []
conf = [list(map(int,input().split())) for _ in range(n)]
conf.sort(key = lambda x:(x[1], x[0]))
count = 0
finish = 0
for i in range(n):
    if finish <= conf[i][0]:
        count += 1
        finish = conf[i][1]
print(count)