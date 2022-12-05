def solution(N, number):
    answer = -1
    num_set = []
    for i in range(1,9):
        case = set()
        point = int(str(N) * i)
        case.add(point)
        for j in range(0,i-1):
            for a in num_set[j]:
                for b in num_set[j-1]:
                    case.add(a-b)
                    case.add(a+b)
                    case.add(a*b)
                    if b != 0:
                        case.add(a//b)
        print(num_set)
        if number in case:
            answer = i
            break
        
        num_set.append(case)
                
    
    
    return answer


print(solution(1, 8))