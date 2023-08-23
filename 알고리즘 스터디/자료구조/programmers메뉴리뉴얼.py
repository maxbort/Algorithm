from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        menu_count = {}  # 각 조합의 등장 횟수를 저장할 딕셔너리

        for order in orders:
            if len(order) < i:  # 최소 메뉴수 보다 조합을 적게 선택한 경우 건너뜀
                continue
            
            # 메뉴 조합을 정렬하여 키로 사용
            for combo in combinations(sorted(order), i):
                menu = "".join(combo)
                menu_count[menu] = menu_count.get(menu, 0) + 1
        
        # 등장 횟수가 가장 많은 조합을 선택
        max_count = max(menu_count.values(), default=0)
        if max_count >= 2:
            answer += [menu for menu, count in menu_count.items() if count == max_count]

    answer.sort()  # 결과를 오름차순 정렬
    return answer
