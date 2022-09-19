def binary_search(array, start, end, target):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

a.sort()

start = 0
end = n -1
for i in range(len(b)):
    print(binary_search(a, start, end, b[i]))