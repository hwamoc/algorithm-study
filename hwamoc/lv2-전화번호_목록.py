def solution(phone_book):
    phone_book.sort(key=len)

    for i in range(1, len(phone_book)):
        if phone_book[i].find(phone_book[0]) == 0:
            # if phone_book[i].startswith(phone_book[0]):
            return False

    return True

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))