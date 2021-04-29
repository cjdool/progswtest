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

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))