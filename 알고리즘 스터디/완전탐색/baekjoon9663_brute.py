import sys
input = sys.stdin.readline

answer = 0
n = int(input())

dx = [0,0,0,1,-1,1,-1,1,-1]
dy = [0,1,-1,0,0,1,-1,-1,1]

graph = [0] * n

def q_place(a):
    for i in range(a):
        if graph[a] == graph[i] or abs(graph[i] - graph[a]) == abs(i-a):
            return False

    return True


def n_queen(x):
    global answer

    if x == n:
        answer += 1

    else:
        for i in range(n):
            graph[x] = i
            if q_place(x):
                n_queen(x+1)

n_queen(0)
print(answer)
