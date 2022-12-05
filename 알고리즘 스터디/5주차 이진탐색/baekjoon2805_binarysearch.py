n,m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
start = 0    
end = sum(trees)

while start <= end:
    mid = (start + end) // 2
    result = 0
    
    for i in trees:
        if i > mid:
            result += i - mid
        
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)