def binary_search(array, start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None 

n = int(input())
a = list(map(int,input().split()))
a.sort()

m = int(input())
b = list(map(int,input().split()))
c = []
for i in range(len(b)):
    c.append(0)
    
start = 0
end = n-1

for i in range(len(b)):
    if binary_search(a, start, end, b[i]):
        c[i] = 1
    else:
        continue

for i in range(len(c)):
    print(c[i], end=' ')