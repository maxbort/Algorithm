def solution(n,a,b):
    answer = 1
    a_idx = a
    b_idx = b

    while True:
            
        if a_idx % 2 == 1:
            a_idx += 1
        if b_idx % 2 == 1:
            b_idx += 1
        
        if a_idx == b_idx:
            break
        a_idx /= 2
        b_idx /= 2
        
        answer += 1
        

    return answer