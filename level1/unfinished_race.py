def solution(participant, completion):
    answer = ''
    for com in completion:
        participant.remove(com)

    answer = participant[0]

    return answer

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])