import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    phone = []
    for _ in range(n):
        phone.append(input().rstrip())
    phone.sort()
    check = True
    for i in range(n-1):
        length = len(phone[i])
        if phone[i] == phone[i+1][:length]:
            check = False
            break
    
    if check:
        print("YES")
    else:
        print("NO")