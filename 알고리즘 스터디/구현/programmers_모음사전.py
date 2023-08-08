import itertools
def solution(word):
    answer = 0
    # alpha = {'A':0,'E':1, 'I':2,'O':3,'I':4}
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1,6):
        for j in itertools.product(alpha,repeat=i):
            words.append(''.join(list(j)))
    words.sort()
    # words.sort() 
    #print(words)
    answer = words.index(word)+1
#     for i in words:
#         answer += 1
#         if i == 'word':
#             break
    
    return answer