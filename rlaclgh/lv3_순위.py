from collections import deque
def solution(n, results):
    win =[ [] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    for x,y in results:
        win[x].append(y)
        lose[y].append(x)
    
    for i in range(1, n+1):
        Q = deque(win[i])
        while Q:
            x = Q.popleft()
            for j in win[x]:
                if j not in win[i]:
                    win[i].append(j)
                    Q.append(j)

        QQ = deque(lose[i])
        while QQ:
            x = QQ.popleft()
            for j in lose[x]:
                if j not in lose[i]:
                    lose[i].append(j)
                    QQ.append(j)
    
    temp = []
    for i in range(1,n+1):
        temp.append(len(win[i])+len(lose[i]))
    
    
    return temp.count(n-1)