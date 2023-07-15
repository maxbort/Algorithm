def solution(places):
    answer = []
    temp = [[] for _ in range(5)]
    for i in range(5):
        for j in places[i]:
            temp[i].append(list(j))
    dx = [-1, -1, -1, 0, 0, 1, 1, 1,0,0,-2,2]
    dy = [-1, 0, 1, 1, -1, -1, 0, 1,2,-2,0,0]

    
    for i in range(5):
        flag = True
        if flag:
            for x in range(5):
                if flag:
                    for y in range(5):        
                        if places[i][x][y] == 'P':
                            for j in range(12):
                                nx = x + dx[j]
                                ny = y + dy[j]
                                if 0 <= nx < 5 and 0 <= ny < 5:
                                    if places[i][nx][ny] == 'P':
                                        if nx-x == -2:
                                            if places[i][x-1][y] == 'X':
                                                continue
                                            else:
                                                flag = False
                                                break
                                        if nx - x == 2:
                                            if places[i][x+1][y] == 'X':
                                                continue
                                            else:
                                                flag = False
                                                break
                                        if ny-y == -2:
                                            if places[i][x][y-1] == 'X':
                                                continue
                                            else:
                                                flag = False
                                                break
                                        if ny - y== 2:
                                            if places[i][x][y+1] == 'X':
                                                continue
                                            else:
                                                flag = False
                                                break
                                                
                                        if abs(nx-x) == 1 and abs(ny-y) == 1:
                                            if places[i][nx][y] != 'X' or places[i][x][ny] != 'X':
                                                flag = False
                                                break
                                            else:
                                                continue              
                                        else:
                                            flag = False
                                            break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
                                    
    return answer