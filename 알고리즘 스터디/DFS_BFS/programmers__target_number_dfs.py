
def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    def dfs(cnt, result):
        global answer
        if cnt == n:
            if result == target:
                answer += 1
                return
        else:
            dfs(cnt+1, result + numbers[cnt])
            dfs(cnt+1, result - numbers[cnt])
    
    
    dfs(0,0)
    
    return answer