def solution(a, b, g, s, w, t):
    answer = float('inf')
    start = 0 
    end = 10**15
    # a는 필요 금, b는 필요 은, g는 도시 당 금 보유량, s는 도시당 은 보유량
    # w는 도시당 트럭이 옮길 수 있는 최대량, t는 이동 시간
    while start <= end:
        mid = (start+end) // 2
        max_gold = 0
        max_silver = 0
        min_gold = 0
        min_silver = 0
        
        for i in range(len(t)):
            c = (mid - t[i]) // (2 * t[i]) + 1
            if g[i] - c * w[i] <= 0:
                max_gold += g[i]
            else:
                max_gold += c * w[i]

            if g[i] - c * w[i] <= 0:
                min_silver += min(s[i], abs(g[i] - c * w[i]))
            else:
                min_silver += 0

            if s[i] - c * w[i] <= 0:
                max_silver += s[i]
            else:
                max_silver += c * w[i]

            if s[i] - c * w[i] <= 0:
                min_gold += min(g[i], abs(s[i] - c * w[i]))
            else:
                min_gold += 0

            if max_gold >= a and max_silver >= b and max_gold + min_silver >= a+b:
                end = mid - 1
                answer = min(answer,min)
            else:
                start = mid+1
    return answer

print(solution(10, 10, [100], [100], [7], [10])) # 50    
        
    