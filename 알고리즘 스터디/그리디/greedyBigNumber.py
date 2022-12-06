n,m,k = map(int,input().split())
answer =0
num=list(map(int,input().split()))
num.sort()

a = num[n-1]
b = num[n-2]

cnt = int(m/(k+1))

answer += a * cnt*3
answer += b*cnt
answer += a * int(m%(k+1))

print(answer)