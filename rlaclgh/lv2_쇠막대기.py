def solution(arrangement):
    arrangement = arrangement.replace('()','L')
    print(arrangement)
    answer = arrangement.count('(')
    for i in range(len(arrangement)):
        if arrangement[i] =='L':
            a = arrangement[:i].count('(')
            b = arrangement[:i].count(')')
            answer += (a-b)
        
    
    return answer