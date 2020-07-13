def solution(clothes):
    dict ={}
    
    for x,y in clothes:
        dict[y] = dict.get(y,1) + 1
    
    answer = 1
    for x,y in dict.items():
        answer *= y
    
    return answer- 1