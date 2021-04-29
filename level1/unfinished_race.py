def solution(participant, completion):
    participant.sort()
    completion.sort()

    for part, com in zip(participant, completion):
        if part != com:
            return part

    return participant[-1]

'''
from collections import Counter

def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
'''

'''
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
'''


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))