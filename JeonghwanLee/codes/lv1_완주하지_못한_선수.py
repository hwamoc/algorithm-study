def solution(participant, completion):
    answer = ''
    part = {}
    comp = {}
    for elem in participant:
        if elem in part:
            part[elem]+=1
        else:
            part[elem]=1
    
    for elem in completion:
        if elem in comp:
            comp[elem]+=1
        else:
            comp[elem]=1
    
    for elem in participant:
        if elem not in comp:
            return elem
        elif part[elem]!=comp[elem]:
            return elem
    
    return answer