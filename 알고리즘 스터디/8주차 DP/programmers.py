
record  = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer = []
    for i in range(len(record)-1, 0, -1):
        if record[i].split(' ')[0] == 'Change': 
            for j in range(i, 0, -1):
                if record[i].split(' ')[1] == record[j].split(' ')[1]:
                    if record[i].split(' ')[2] != record[j].split(' ')[2]:
                        a = record[i].split(' ')[2]
                        b = record[j].split(' ')[2]
                        record[j].replace(a, b)
                        print(record)
    print(record)
    for i in range(len(record) - 1):
        if record[i].split(' ') == "Enter":
            nick = record[i].split(' ')[2]
            a = nick + "님이 들어왔습니다."
            answer.append(a)
        elif record[i].split(' ') == "Leave":
            nick = record[i].split(' ')[2]
            a = nick + "님이 나갔습니다."
            answer.append(a)
        
    return answer

answer = solution(record)
print(answer)