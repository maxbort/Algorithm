import sys
import copy
input = sys.stdin.readline

sdocu = []

for _ in range(9):
    sdocu.append(list(map(int,str(input().rstrip()))))

num_list = [1,2,3,4,5,6,7,8,9]

no_num = []

for i in range(9):
    for j in range(9):
        if not sdocu[i][j]:
            no_num.append((i,j))

def fill_blank(a):
    if len(no_num) == a:
        for i in sdocu:
            print(*i, sep='')
        sys.exit()
    
    x, y = no_num[a]
    dx,dy = x//3, y//3
    temp = copy.deepcopy(num_list)
    
    for i in range(dx*3, (dx+1)*3):
        for j in range(dy*3, (dy+1)*3):
            if sdocu[i][j] in temp:
                temp.remove(sdocu[i][j])
           
    
    for i in range(9):
        if sdocu[x][i] in temp:
            temp.remove(sdocu[x][i])
        if sdocu[i][y] in temp:
            temp.remove(sdocu[i][y])
    
    
    for i in temp:
        sdocu[x][y] = i
        fill_blank(a+1)
    sdocu[x][y] = 0
    
fill_blank(0)   