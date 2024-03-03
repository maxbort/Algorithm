def solution(files):
    answer = []
    num_list = [str(i) for i in range(10)]
    conv_files = []
    head,num,tail = '','',''
    for i in files:
        for j in range(len(i)):
            if i[j] in num_list:
                head = i[:j]
                num = i[j:]
                for k in range(len(num)):
                    if num[k] not in num_list:
                        print(num[k])
                        tail = num[k:]
                        num = num[:k]
                        break
                conv_files.append([head,num,tail])
                head,num,tail = '','',''
                break
        
    conv_files.sort(key= lambda x : (x[0].upper(),int(x[1])))
    print(conv_files)
    for i in conv_files:
        answer.append(''.join(i))
    
    return answer
