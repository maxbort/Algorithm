import itertools

def solution(e):
    
    def ope(n,m,o):
        if o == '+':
            return str(int(n) + int(m))
        elif o == '-':
            return str(int(n) - int(m)) 
        else:
            return str(int(n)*int(m))
    answer = 0
    operator = ['*', '+', '-']
    operator = itertools.permutations(operator,3)
    operator = list(operator)
    
    for i in operator:
        e2 = e
        for j in i:
            print(j)
        #     for k in range(len(e)):
        #         if j == e2[k]:
        #             d = eval(e[k-1:k+2])
        #             e2[k-1] = -1
        #             e2[k+1] = -1
        #             e2[k] = d
        #     for z in e:
        #         if z < 0:
        #             e2.remove(z)
        # if answer < sum(e2):
        #     answer = sum(e2)
    
    
    
    return answer

