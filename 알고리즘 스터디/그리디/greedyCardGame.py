n,m = map(int,input().split())

graph=[]
for _ in range(m):
    graph.append(list(map(int,input().split())))

answer =[]
for i in graph:
    answer.append(min(i))
print(max(answer))