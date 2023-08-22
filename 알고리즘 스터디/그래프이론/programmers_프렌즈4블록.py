from collections import deque

def solution(m, n, board):
    answer = 0
    graph = [list(board[i]) for i in range(m)]
    mv = [[0, 1], [1, 0], [1, 1]]
    q = deque()
    del_block = set()
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                check =graph[i][j]
                if check == '@':
                    continue
                else:
                    nx, ny = i, j
                    q.append((nx, ny))
                    for l in range(3):
                        a, b = mv[l]
                        mx = nx + a
                        my = ny + b
                        if graph[mx][my] != check:
                            q.clear()
                            break
                        q.append((mx, my))
                    if len(q) == 4:
                        while q:
                            a, b = q.popleft()
                            del_block.add((a, b))
                    
        if del_block:
            answer += len(del_block)
            for i,j in del_block:
                graph[i][j] = '@'
            del_block= set()  
        else:
            return answer
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if graph[i][j] != '@' and graph[i + 1][j] == '@':
                        graph[i+1][j] = graph[i][j]
                        graph[i][j] = '@'
                        moved += 1
            if moved == 0:
                break


