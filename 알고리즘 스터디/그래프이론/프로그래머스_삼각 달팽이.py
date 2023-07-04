def solution(n):
    answer = []
    tmp = [[] for j in range(1,n+1)]
    temp = 1
    for i in range(n):
        tmp[i] = [0] * temp
        temp +=1
        
    dx = -1
    dy = 0
    start = 1
    answer = []
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                dx += 1
            elif i % 3 == 1:
                dy += 1
            else:
                dx -= 1
                dy -= 1
            tmp[dx][dy]= start
            start += 1
    
    for i in tmp:
        answer += i
        
        
    
    return answer