n,m = map(int,input().split())

tt = list(map(int,input().split()))
tt.sort()

start = 1
end = max(tt)

def binary(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        tteok = 0
        for i in arr:
            if i > mid:
                tteok += (i-mid)
            else:
                pass
        if tteok > target:
            start = mid + 1
        elif tteok == target:
            return mid
        else:
            end = mid - 1
    return None


print(binary(tt,m,start,end))