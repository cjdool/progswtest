def dfind (answer, k, step):
    cnt = 0
    for i in range(k+1, len(answer)):
        if answer[i] == 'O':
            cnt += 1
            if cnt == step:
                return i


def ufind (answer, k, step):
    cnt = 0
    for i in range(k-1, -1, -1):
        if answer[i] == 'O':
            cnt += 1
            if cnt == step:
                return i


def solution(n, k, cmd):
    answer = ['O'] * n
    clipboard = []
    for c in cmd:
        if c[0] == 'D':
            u, x = c.split(' ')
            k = dfind(answer, k, int(x))
        elif c[0] == 'U':
            u, x = c.split(' ')
            k = ufind(answer, k, int(x))
        elif c[0] == 'C':
            answer[k] = 'X'
            clipboard.append(k)
            temp = dfind(answer, k, 1)
            if temp is None:
                k = ufind(answer, k, 1)
            else:
                k = temp
        else: # c[0] == 'Z'
            if clipboard:
                revnum = clipboard.pop()
                answer[revnum] = 'O'

    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))