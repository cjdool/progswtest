from collections import deque


def ck(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            cnt += 1
            if cnt > 1:
                return False

    return True


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0] * len(words)
    queue = deque()
    queue.append((begin, 0))
    if begin in words:
        visited[words.index(begin)] = 1

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for idx, w in enumerate(words):
            if visited[idx] == 0 and ck(word, w):
                queue.append((w, cnt+1))
                visited[idx] = 1


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
