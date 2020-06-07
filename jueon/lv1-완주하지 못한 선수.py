def solution(participant, completion):
    hash={}
    for i in participant:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in completion:
        hash[i]-=1
    for i in hash:
        if hash[i]>0: return i
     
    return ''