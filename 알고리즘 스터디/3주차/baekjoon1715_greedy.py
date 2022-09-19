n = int(input())

list = []
for _ in range(n):
    list.append(int(input()))

d = 2
cnt = list[0] + list[1]

while True:
    if d >= len(list):
        break
    a = cnt + list[d]
    cnt += a
    d += 1

print(cnt)