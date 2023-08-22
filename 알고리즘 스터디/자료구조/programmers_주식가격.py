def solution(prices):
    answer = [0] * len(prices)
    temp = []
    check = 0
    
    for i in range(len(prices)):
        check = prices[i]
        for j in range(i,len(prices)-1):
            if check <= prices[j]:
                answer[i] += 1
            else:
                break
    
    
    return answer