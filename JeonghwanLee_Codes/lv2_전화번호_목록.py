def solution(phone_book):
    answer = True
    for i,phone in enumerate(phone_book):
        length = len(phone)
        for j,_phone in enumerate(phone_book):
            if length>=len(_phone):
                continue
            else:
                if phone == _phone[:length]:
                    return False
                
    return answer