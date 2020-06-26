def solution(n, lost, reserve):
    ch =[0] * (n+2)
    cnt = 0
    inter = set(lost) & set(reserve)
    for i in reserve:    
        ch[i] = 1
    for i in inter:
        ch[i] =0
    for i in set(lost) - set(inter):
        if ch[i-1] == 1:
            ch[i-1] =0
            cnt +=1
        elif ch[i+1] == 1:
            ch[i+1] =0
            cnt +=1
    return n - len(lost) + cnt +len(inter)