def solution(s):
    answer = []
    for i in range(1, len(s)+1):
        a = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s)+i, i): 
            if tmp==s[j:i+j]:
                cnt+=1 
            else: 
                if cnt!=1: 
                    a = a + str(cnt) + tmp 
                else:
                    a = a + tmp
                tmp=s[j:j+i]
                cnt = 1
        answer.append(len(a))
    
    
    
    return min(answer)