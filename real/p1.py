def trans(strlist):
    retval = ''
    while strlist:
        if strlist[0] == 'z':
            retval += '0'
            strlist = strlist[4:]
        elif strlist[0] == 'o':
            retval += '1'
            strlist = strlist[3:]
        elif strlist[0] == 't':
            if strlist[1] == 'w':
                retval += '2'
                strlist = strlist[3:]
            else:
                retval += '3'
                strlist = strlist[5:]
        elif strlist[0] == 'f':
            if strlist[1] == 'o':
                retval += '4'
                strlist = strlist[4:]
            else:
                retval += '5'
                strlist = strlist[4:]
        elif strlist[0] == 's':
            if strlist[1] == 'i':
                retval += '6'
                strlist = strlist[3:]
            else:
                retval += '7'
                strlist = strlist[5:]
        elif strlist[0] == 'e':
            retval += '8'
            strlist = strlist[5:]
        elif strlist[0] == 'n':
            retval += '9'
            strlist = strlist[4:]
    return retval


def solution(s):
    answer = ''
    temp = []
    for c in s:
        if c.isdigit():
            if temp:
                answer += trans(temp)
                temp = []
            answer += c
        else:
            temp.append(c)

    if temp:
        answer += trans(temp)
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
