from heapq import heappop, heappush

def dijkstra(start, target):
    q = []
    distance=[10**9]*(N+1)
    distance[start]=0
    heappush(q, [0, start])

    while q:
        dist, curr = heappop(q)
        if distance[curr]<dist:
            continue

        for next_c, next_node in graph[curr]:
            cost = dist+next_c
            if cost<distance[next_node]:
                distance[next_node]=cost
                heappush(q, ([cost, next_node]))

    return distance[target]




if __name__=="__main__":
    N, M = map(int,input().split())
    graph=[[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())

        if a==b : continue

        graph[a].append([c, b])

    start, target = map(int, input().split())
    print(dijkstra(start, target))