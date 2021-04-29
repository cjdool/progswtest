def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    length = len(phone_book)
    for i in range(length):
        pivot = phone_book[i]
        for j in range(i+1, length):
            comp = phone_book[j]
            if len(pivot) < len(comp) and pivot == comp[0:len(pivot)]:
                return False

    return answer

solution(["119", "97674223", "1195524421"])