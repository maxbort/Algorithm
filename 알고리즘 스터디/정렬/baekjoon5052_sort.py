import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    k = int(input())
    pl = []
    for j in range(k):
        pl.append(input().strip())
    pl.sort() # 받은 전화번호 리스트 
    for i in range(len(pl)-1): 
        # 확인하는 i가 리스트의 다른 원소들의 접두어인지 확인하기 위한 변수 word
        check = True # 검사 중 한번이라도 원소가 접두어로 됐을 경우 반복문 탈출을 위한 변수
        word = pl[i]
        for j in range(i+1,len(pl)):
            if pl[i] == pl[j][:len(word)]: # 숫자 자릿수 만큼 비교 후 일치할 경우 check = False
                check = False
                break
        if check == False: # check가 false면 접두어가 있는경우 이므로 no 출력 후 반복문 탈출
            print('NO')
            break
    if check:    # 전체를 검사 후 check가 True면 접두어가 없으므로 yes
        print('YES')
            