def solution(number, k):
    num = list(map(int,str(number)))
    stack =  []
    
    for x in num:
        while stack and k > 0 and stack[-1]<x:
            stack.pop()
            k -= 1
        stack.append(x)
    
    if k !=0:
        stack = stack[:-k]
    
    res = ''.join(map(str,stack))
    return res