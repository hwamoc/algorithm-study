def solution(phone_book):
    hash={}
    temp=sorted(phone_book) #작은 원소먼저 접두사로 찾을 수 있도록 정렬한다.
    for p in temp: 
        #hash 딕셔너리에 있으면 FALSE를 리턴하고 없으면 추가한다. 
        for h in hash:
            if h in p:
                return False
        hash[p]=1
    return True