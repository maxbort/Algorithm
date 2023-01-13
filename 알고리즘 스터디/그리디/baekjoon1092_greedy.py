n = int(input())
crane = list(map(int,input().split()))   
m = int(input())
box = list(map(int,input().split()))                 

crane.sort(reverse=True)
box.sort(reverse=True)
time = 0

check_crane = 0
if max(box) > max(crane):
    print(-1)
else:
    while box:
        if not box:
            break
        for i in crane:
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
    time += 1
    print(time)
