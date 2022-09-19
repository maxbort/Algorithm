

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    blacket = []
    
    for i in moves:
        for j in range(5):
            if board[j][i-1] == 0:
                continue
            else:
                if not blacket:
                    blacket.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
                else:
                    a = blacket.pop()
                    if board[j][i-1] == a:
                        answer += 2
                        board[j][i-1] = 0
                        break
                    else:
                        blacket.append(a)
                        blacket.append(board[j][i-1])
                        board[j][i-1] = 0
                        break
        
    print(board)
    return answer
print(solution(board,moves))
