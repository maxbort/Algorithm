N = 4
stages = [4,4,4,4,4]

def solution(N, stages):
    users = len(stages)
    scf = []
    for num in range(N+1):
        scf.append([0,num])
        
    for i in range(N+1):
        fail_user = stages.count(i)
        fail_rate = fail_user / users
        
        scf[i] = [fail_rate, i]
        
        users -= fail_user
        
    scf.pop(0)
    scf.sort(key=lambda x : (-x[0],x[1]))
    answer =[]
    for i in scf:
        answer.append(i[1])
    print(answer)




# def solution(N, stages):
#     users = len(stages)
#     scf = []
#     for i in range(N+1):
#         scf.append([0, i])
#     stages.sort()
#     stagecheck = 0 
#     answer = []
#     for stage in stages:
#         if stagecheck == stage:
#             pass
#         else:
#             if stage > N:
#                 scf[stage-1] = [0,stage-1]
#                 break
#             stagecheck = stage
#             fail_user = stages.count(stage)
#             if fail_user == 0:
#                 scf[stage] = [0,stage]
#                 pass
#             fail_rate = fail_user / users
#             users -= fail_user
#             scf[stage] = [fail_rate,stage]
#     scf.pop(0)
#     scf.sort(key=lambda x : [-x[0], x[1]])
#     print(scf)
#     for i in scf:
#         answer.append(i[1])
#     print(answer)
    

    
solution(N,stages)