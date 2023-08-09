# import sys
# from itertools import combinations

# input = sys.stdin.readline

# l,c = map(int,input().split())
# word = list(map(str,input().split()))
# word.sort()
# answer = []
# vowel = ['a','e','i','o','u']

# def solution(cnt, idx):
#     if cnt == l:
#         a, b = 0, 0
        
#         for i in range(l):
#             if answer[i] in vowel:
#                 a += 1
#             else:
#                 b += 1
#         if a >= 1 and b >= 2:
#             print("".join(answer))
#         return
#     for i in range(idx,c):
#         answer.append(word[i])
#         solution(cnt+1,i+1)
#         answer.pop()
# solution(0,0)

import sys
from itertools import combinations
input = sys.stdin.readline

l,c = map(int,input().split())
word = list(map(str,input().split()))
vowel = ['a','e','i','o','u']
word.sort()
a = list(combinations(word,l))
a.sort()
for i in a:
    num_vowel = sum(1 for j in i if j in vowel)
    num_con = l - num_vowel
    
    if num_con >= 2 and num_vowel >= 1:
        print("".join(i))
