n = int(input())

for i in range(n):
    k = int(input())
    pl = []
    for j in range(k):
        pl.append(str(input())) # 전화번호를 문자열로 처리하기 위해 str로 받음
    pl.sort(key=lambda x : len(x)) # 받은 전화번호 리스트를 문자열 길이 순으로 정렬
    
    for i in range(len(pl)-1): 
        # 확인하는 문자열 i가 리스트의 다른 원소들의 접두어인지 확인하기 위한 변수 cnt
        check = True # 검사 중 한번이라도 원소가 접두어로 됐을 경우 반복문 탈출을 위한 변수
        cnt = 0
        for j in range(i+1,len(pl)):
            for k in range(len(pl[i])): # k는 위에서의 i의 길이만큼 순회
                if pl[i][k] == pl[j][k]: # 문자가 일치할 경우 cnt 1씩 증가
                    cnt += 1
                else: # 한번이라도 일치하지 않는경우는 검사할 필요 x
                    break
            if cnt == len(pl[i]): # 접두어가 있는 경우 이므로 check = False로 하고 반복문 탈출
                check = False
                break
            else:
                cnt = 0
        if check == False: # check가 false면 접두어가 있는경우 이므로 no 출력 후 반복문 탈출
            print('NO')
            break
    if check:    # 전체를 검사 후 check가 True면 접두어가 없으므로 yes
        print('YES')
            