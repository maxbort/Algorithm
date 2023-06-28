from heapq import heappop, heappush

def prim():
    visited=[False]*(N+1)
    q=[]
    heappush(q, [0, 1])
    ret=0

    while q:
        dist, curr=heappop(q)
        if visited[curr]:
            continue
        visited[curr]=True
        ret+=dist

        for next_c, next_node in graph[curr]:
            heappush(q, ([next_c, next_node]))

    return ret



if __name__=="__main__":
    N,M = map(int,input().split())
    graph=[[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())

        if a==b : continue

        graph[a].append([c, b])
        graph[b].append([c, a])
    print(prim())