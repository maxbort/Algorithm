## 1번
def solution(s, N):
    tmp = -1

    for i in range(len(s)):
        num = [a for a in range(1,N+1)]
        flag = True

        if s[i] == str(N):
            if N+i <= len(s)+1:
                for j in s[i:i+N]:
                    if int(j) in num:
                        num.remove(int(j))
                    else:
                        flag = False
                        break

                if tmp < int(s[i:N+i]) and flag:
                    tmp = int(s[i:N+i])

            if i-N >= -1:
                for k in s[i-N+1:i+1]:
                    if int(k) in num:
                        num.remove(int(k))
                    else:
                        flag = False
                        break
                if tmp < int(s[i-N+1:i+1]) and flag:
                    tmp = int(s[i-N+1:i+1])
    answer = tmp


    return answer



### 2번

new_friend = []
tot_rew = 0
visit = [False] * 101

def solution(relationships, target, limit):
    answer = 0
    people = [[] for _ in range(101)]
    for i in relationships:
        people[i[0]].append(i[1])
        people[i[1]].append(i[0])
    already_friend = people[target]

    def dfs(a, b):
        global new_friend, tot_rew, visit
        if b == limit:
            return
        for i in people[a]:
            if i == target:
                continue
            if i in already_friend and not visit[i]:
                tot_rew += 5
                visit[i] = True
                dfs(i, b + 1)
            elif not visit[i]:
                visit[i] = True
                tot_rew += 10
                new_friend.append(i)
                dfs(i, b + 1)

    dfs(target, 0)
    answer = len(new_friend) + tot_rew
    return answer

### 3번
def solution(merchantNames):
    answer = []
    specialInitial = ['&', '(', ')', '.', ',', '-']
    tmp = ''
    for i in merchantNames:
        if ' ' in i:
            i.replace(' ' , '')

    for i in merchantNames:
        if tmp == '':
            tmp = i
        else:
            if tmp in i:
                for j in specialInitial:
                    if j in i:
                        tmp = i
        if tmp not in answer:
            answer.append(tmp)




    return answer