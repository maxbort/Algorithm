v,e = map(int,input().split())

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [0] * (v+1)

edges = []
money = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    edges.append(tuple(map(int,input().split())))
    
edges.sort(key=lambda x: x[2])
temp =0
for edge in edges:
    a,b,cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        money += cost
        temp = cost
print(money - temp)