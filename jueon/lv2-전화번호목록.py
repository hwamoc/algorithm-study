def solution(phone_book):
    
    hash={}
    temp=sorted(phone_book)
    for p in temp:
        for h in hash:
            if h in p:
                return False
        hash[p]=1
    return True