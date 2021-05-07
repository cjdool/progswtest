def solution(new_id):
    answer = ''
    # 1st
    new_id = new_id.lower()
    # 2nd, 3rd
    cnt = 0
    for c in new_id:
        if c.isalpha() or c.isdigit() or c == '-' or c == '_' or c == '.':
            if c == '.':
                cnt += 1
                if cnt > 1:
                    continue
            else:
                cnt = 0
            answer += c
    # 4rd
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5th
    if answer == '':
        answer = 'a'
    # 6th
    if len(answer) > 15:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7th
    if len(answer) == 1:
        answer += answer[-1]
    if len(answer) == 2:
        answer += answer[-1]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
