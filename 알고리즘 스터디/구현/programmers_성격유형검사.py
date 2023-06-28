def solution(survey, choices):
    personality = [['R',0],['T',0],['C',0],['F',0],['J',0],['M',0],['A',0],['N',0]]
    for i in range(len(survey)):
        s = choices[i]
        for j in personality:
            if s < 4:
                if survey[i][0] == j[0]:
                    j[1] += 4-s
            elif s > 4:
                if survey[i][1] == j[0]:
                    j[1] += s-4

    answer = ''
            
    for i in range(0, 8, 2):
        if personality[i][1] >= personality[i+1][1]:
            answer += personality[i][0]
        else:
            answer += personality[i+1][0]

    return answer