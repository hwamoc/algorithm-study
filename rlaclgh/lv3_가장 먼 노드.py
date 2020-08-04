from collections import deque

def solution(n, edge):
    matrix =[  [] for _ in range(n + 1) ]
    distance = [ 0 for _ in range(n+1) ]
    is_visit = [False for _ in range(n+1)]
    is_visit[1] = True
    
    for (a, b) in edge:
        matrix[a].append(b)
        matrix[b].append(a)
    
    Q = deque([1])
    while Q:
        x = Q.popleft()
        for j in matrix[x]:
            if is_visit[j] ==False:
                is_visit[j] = True
                Q.append(j)
                distance[j] = distance[x]+1 
                
    maximum = max(distance)
    
    return distance.count(maximum)

