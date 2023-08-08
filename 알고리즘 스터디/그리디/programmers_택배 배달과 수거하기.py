def solution(cap, n, deliveries, pickups):
    answer = 0
    # cap은 실을 수 있는 최대 상자 수, n은 전체 거리,
    # deliveries는 각 집마다 배달해야되는 상자 수,  pickups는 각 집마다 수거해야할 상자 수
    deli, pick = 0, 0
    
    for i in reversed(range(n)):
        deli += deliveries[i]
        pick += pickups[i]
        
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += 2*(i+1)
            
    return answer 