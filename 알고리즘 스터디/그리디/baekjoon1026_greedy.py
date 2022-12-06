n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

answer = 0
for _ in range(n):
    a = min(A)
    b = max(B)
    answer += a*b
    A.remove(a)
    B.remove(b)


print(answer)