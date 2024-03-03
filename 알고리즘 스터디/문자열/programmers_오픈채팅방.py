def solution(record):
    answer = []
    user = dict()
    commands = []  

    for command in record:
        info = command.split() 
        action, userid = info[0], info[1]
        if action =="Enter" or action == "Change":
            nick = info[2]
            user[userid] = nick
        commands.append((action, userid))

    for a in commands:
        action, userid = a[0], a[1]
        if action == 'Enter':
            answer.append(f'{user[userid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user[userid]}님이 나갔습니다.')

    return answer
