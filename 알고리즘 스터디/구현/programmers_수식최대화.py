import itertools

def solution(expression):
    answer = 0
    operator = ['*', '+', '-']
    operator = itertools.permutations(operator,3)

    print(list(operator))
    
    
    return answer

solution(0)