import sys

input = sys.stdin.readline

n = int(input())

people = []
for _ in range(n):
    people.append(list(map(int,input().split())))


answer = []
for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    answer.append(rank)

for i in answer:
    print(i,end=' ')