def solution(rows, columns, queries):
    matrix= [[] for _ in range(columns)]
    tmp = 1
    for i in range(columns):
        for j in range(rows):
            matrix[i].append(tmp)
            tmp+=1
    answer = []
    for i in queries:
        lx,ly,rx,ry = i
        lx,ly,rx,ry = lx-1, ly-1, rx-1,ry-1
        dx = abs(rx-lx)
        dy = abs(ry - ly)
        mini = float('INF')

        temp = matrix[lx][ly]

        for a in range(1,dy):
            matrix[lx][ly+a] = matrix[lx][ly]+1
        answer.append(mini)
        
        
        
        
    return answer

