from collections import deque

def solution(queue1, queue2):
#     answer = 0
#     limit = 300000
#     all_q = queue1 + queue2
#     check_point = sum(all_q)
#     if check_point % 2 == 1:
#         answer = -1
#         return answer
#     check_point = check_point//2
    
#     answer = float('inf')
    

    limit = 300000
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    q1_sum = sum(q1)
    q2_sum = sum(q2)
    tot = q1_sum + q2_sum
    
    if tot % 2 == 1:
        answer = -1
        return answer
    
    while True:
        if q1_sum > q2_sum:
            check = q1.popleft()
            q2.append(check)
            q1_sum -= check
            q2_sum += check
            answer+=1
            
        elif q1_sum < q2_sum:
            check = q2.popleft()
            q1.append(check)
            q1_sum += check
            q2_sum -= check
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
        
    return answer