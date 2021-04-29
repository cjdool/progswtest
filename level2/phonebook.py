def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for i in range(length-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

'''
# using zip iter
def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
'''

'''
# using hashmap
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
'''

solution(["119", "97674223", "1195524421"])