n = int(input())   
a = input().split()
j =1
for i in range(n):
    a[i] = int(a[i])
d = int(a[0])

while j != n:
    if d >= int(a[j]):
        d = int(a[j])
    j += 1
    
print(int(d))
