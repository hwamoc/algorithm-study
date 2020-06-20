#코딩테스트 고득점 Kit_해시
def solution(participant, completion):
    hash={} #파이썬 내 해시 자료구조인 딕셔너리를 사용했음
    #participant를 딕셔너리에 추가한다. 이미 저장되어있을 경우 추가.
    for i in participant:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    #completion내 요소를 탐색하며 해쉬 딕셔너리에 해당하는 key가 있을 경우 value를 감소한다.
    for i in completion:
        hash[i]-=1
    #hash에 0이상의 값이 남아있으면 completion에 없는 원소임.
    for i in hash:
        if hash[i]>0: return i
     
    return ''