from heapq import heappop, heappush

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x,y=find(x),find(y)
    parent[x]=y

def kruskal():
    cost=0

    while q:
        dist, v1, v2 = heappop(q)
        if find(v1) == find(v2): # 사이클 검사
            continue
        else:
            cost += dist
            union(v1, v2)
    return cost

if __name__=="__main__":
    N,M  = map(int,input().split()) 
    
    q=[]
    for _ in range(M):
        a, b, c = map(int, input().split())
        heappush(q, [c, b, a])
    
    parent = [i for i in range(N+1)]
    
    print(kruskal())