def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for i in range(length-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

'''
def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
'''

solution(["119", "97674223", "1195524421"])