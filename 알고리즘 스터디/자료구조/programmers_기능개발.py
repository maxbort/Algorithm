import math
def solution(progresses, speeds):
    answer = []
    total = 100
    days = 0
    cnt = 1
    for a, b in zip(progresses, speeds):
        rest = total - a
        if days == 0:
            days = rest / b
            days = math.ceil(days)
        else:
            if days >= rest/b:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
                days = math.ceil(rest / b)
    answer.append(cnt)
        
    return answer