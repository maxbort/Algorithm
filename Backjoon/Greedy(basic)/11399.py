n = int(input())
person = list(map(int,input().split()))
person.sort()
delay = 0
total = 0
for i in range(n):
    delay += person[i]
    total += delay

print(total)
