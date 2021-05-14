def solution(name):
    answer = 0
    cursor = 0
    change = []
    for c in name:
        change.append(min(ord(c)-ord('A'), ord('Z')- ord(c)+1))

    while True:
        answer += change[cursor]
        change[cursor] = 0
        if sum(change) == 0:
            return answer

        left, right = 1, 1
        while change[cursor - left] == 0:
            left += 1
        while change[cursor + right] == 0:
            right += 1

        if left < right:
            answer += left
            cursor -= left
        else:
            answer += right
            cursor += right


print(solution("JEROEN"))
print(solution("JAN"))
print(solution('ZZAAAZZ'))
