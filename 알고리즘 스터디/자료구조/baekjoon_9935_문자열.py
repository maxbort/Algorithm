# import sys
# input = sys.stdin.readline

# first = input().rstrip()
# bomb = input().rstrip()
# after = first
# n = len(bomb)
# flag = True

# while flag:
#     for i in range(len(after)):
        
#         if after[i:i+n] == bomb:
#             a = after[0:i]
#             b = after[i+n:]
#             after = a+b
#             if not after:
#                 flag=False
#             break
#         if i > len(after)-n:
#             flag = False
#             break
    
# if after != '':
#     print(after)
# else:
#     print('FRULA')

# 스택을 활용해서 효율성을 올림
import sys
input = sys.stdin.readline

def remove_pattern(text, pattern):
    stack = []
    pattern_length = len(pattern)
    for char in text:
        stack.append(char)
        if len(stack) >= pattern_length:
            if stack[-pattern_length:] == list(pattern):
                del stack[-pattern_length:]
    return stack

first = input().rstrip()
bomb = input().rstrip()

after = remove_pattern(first, bomb)
if after:
    print(''.join(after))
else:
    print('FRULA')

            