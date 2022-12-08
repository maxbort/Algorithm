n = int(input())
A = list(map(int,input().split()))
A.sort()

m = int(input())
B = list(map(int,input().split()))

def binary(arr,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return None
            
            
for i in B:
    result = binary(A, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no',end = ' ')

