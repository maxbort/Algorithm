import sys

input = sys.stdin.readline

st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
st1.extend(reversed(st2))
print(''.join(st1))


# import sys
# input = sys.stdin.readline

# s = str(input().rstrip())
# n = int(input())
# command = [list(map(str,input().split())) for _ in range(n)]

# cursor = len(s)


# for i in command:
#     if i[0] == 'L':
#         if 0 <= cursor:
#             cursor -=1
#     elif i[0] == 'D':
#         if cursor < len(s):
#             cursor += 1
#     elif i[0] == 'B':
#         if cursor == -1:
#             continue
#         elif cursor == len(s):
#             s = s[:cursor-1]
#             cursor -=1
#         else:
#             s = s[:cursor-1] + s[cursor:]
#             cursor -= 1
#     elif i[0] == 'P':
#         if cursor == -1:
#             s = i[1]+s
#             cursor += 1
#         elif cursor == len(s):
#             s = s + i[1]
#             cursor += 1
#         else:
#             s = s[:cursor] + i[1] + s[cursor]
#             cursor += 1
# print(s)





















# for i in command:
#     if i[0] == 'L':
#         if 0 < cursor <= len(s)-1:
#             cursor -=1
#             print(cursor, "L일 경우")
#     elif i[0] == 'D':
#         if 0 <=cursor < len(s)-1:
#             cursor += 1
#             print(cursor, "D일 경우")

#     elif i[0] == 'B':
#         if cursor == 0:
#             continue
#         elif cursor == len(s) - 1:
#             s = s[:cursor]
#             cursor -=1
#             print(s)
#             print(cursor, "B일경우")
#         else:
#             tmp = s[:cursor].strip()
#             tmp2 = s[cursor+1:].strip()
#             s = tmp + tmp2
#             if cursor > 0:
#                 cursor -= 1
#             print(s)
#             print(cursor, "B일경우")
#     elif i[0] == 'P':
#         if cursor == 0:
#             s = i[1] + s
#             print(s)
#             cursor += 1
#         elif cursor == len(s)-1:
#             s = s + i[1]
#             cursor+=1
#             print(s)
            
#         else:
#             tmp = s[:cursor+1].strip()
#             tmp2 = s[cursor+1:].strip()
#             print(tmp)
#             print(tmp2)
#             tmp = tmp + str(i[1])
#             s = tmp + tmp2
#             cursor += 1
#             print(s)
#             print(cursor, 'P일 경우')
# print(s,end='')
