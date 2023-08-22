import sys

input = sys.stdin.readline

n = int(input())

dp = []
building = list(map(int,input().split()))


def check_building(s_x,s_y,e_x,e_y,inc):
    temp_inc = (e_y-s_y)/(e_x-s_x)

    if e_x > s_x:
        if inc >= 0:
            if temp_inc > 0:
                if temp_inc > inc:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if temp_inc >= 0:
                return True
            else:
                if abs(temp_inc) < abs(inc):
                    return True
    else:
        if inc < 0:
            if temp_inc >= 0:
                return False
            else:
                if abs(temp_inc) > abs(inc):
                    return True
        else:
            if temp_inc < 0:
                return True
            else:
                if abs(temp_inc) < abs(inc):
                    return True

            
check = True
for i in range(n):
    cnt = 0
    a = 0
    check = True
    for j in range(i+1,n+1):
        if j == n:
            break
        if cnt == 0:
            cnt+=1
            a = (building[j]-building[i]) / (j-i)
            continue
        
        check = check_building(i,building[i],j,building[j],a)
        if check:
            a = (building[j]-building[i]) / (j-i)
            cnt += 1

  
    a = 0
    check = True
    cnt2 = 0
    for k in range(i-1,-1,-1):
        if k == -1 :
            break
        if cnt2 == 0:
            cnt2 += 1
            a = (building[k]-building[i]) / (k-i)
            continue
        
        check =  check_building(i,building[i],k,building[k],a)
        if check:
            a = (building[k]-building[i]) / (k-i)
            cnt2 += 1

    dp.append(cnt+cnt2)
print(max(dp))