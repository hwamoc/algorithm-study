def solution(n, times):
    times.sort()
    lt = 0
    rt = times[0] * n
    
    while rt -lt !=1:
        mid = (lt+rt) //2
        temp = [mid // x for x in times]
        if sum(temp) >= n :
            rt = mid
        else:
            lt = mid
            
    return rt
        