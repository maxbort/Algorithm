import itertools


def solution(expression):
    operator = ['*', '+', '-']
    operator = itertools.permutations(operator,3)
    operator = list(operator)
    temp = []
    answer = 0
    for i in operator:
        a = i[2]
        b = i[1]
        tmp = []
        for j in expression.split(a):
            tmp1 = []
            for k in j.split(b):
                tmp1.append('(' + k + ')')
            
            tmp.append('(' + b.join(tmp1) + ')')
        last = []
        
        last.append('(' + a.join(tmp) + ')')    
            
        # print(a.join(last))
        print(''.join(last))
        cal = eval(''.join(last))
        print(cal)
        if answer < abs(int(cal)):
            answer = abs(int(cal))
        print(answer)
        
    return answer