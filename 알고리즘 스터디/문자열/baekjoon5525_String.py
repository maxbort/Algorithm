# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# s = input().rstrip()


# p='IO' * n + 'I'
# answer = 0


# for i in range(m):
    
#     if s[i] == 'I':
#         if i + len(p) > m:
#             break
#         if str(s[i:i+len(p)]) == p:
#             answer += 1
#             i = i+len(p)
# print(answer)

import sys

# 패턴의 실패 함수를 구축하는 함수
def build_failure_table(pattern):
    m = len(pattern)
    failure = [0] * m  # 실패 함수를 저장할 배열 초기화
    j = 0  # 실패 함수 값을 계산하기 위한 변수

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            # j-1까지의 부분 패턴에서 가장 긴 접두사와 접미사의 길이를 이용하여 j값을 갱신
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            failure[i] = j  # 실패 함수 값 저장

    return failure

# KMP 알고리즘을 사용하여 패턴 매칭을 수행하는 함수
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    failure = build_failure_table(pattern)  # 실패 함수 구축
    count = 0  # 패턴이 발생한 횟수를 저장하는 변수
    j = 0  # 패턴 매칭을 위한 변수

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            # j-1까지의 부분 패턴에서 가장 긴 접두사와 접미사의 길이를 이용하여 j값을 갱신
            j = failure[j - 1]
            k = text[i]
            l = pattern[j]
            z = failure[j]
        if text[i] == pattern[j]:
            if j == m - 1:
                # 패턴의 끝에 도달한 경우 한 번의 일치가 발생한 것으로 간주하여 count 증가
                count += 1
                j = failure[j]  # j값 초기화하여 다음 패턴 매칭을 수행
            else:
                j += 1  # 다음 문자와 패턴의 일치 여부를 확인하기 위해 j값 증가

    return count

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

pattern = 'IO' * n + 'I'  # 검색할 패턴 설정
answer = kmp_search(s, pattern)  # KMP 알고리즘을 사용하여 패턴 매칭 수행
print(answer)
