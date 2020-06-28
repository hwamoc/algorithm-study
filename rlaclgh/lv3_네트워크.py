from collections import deque

def solution(n,computers):
    ch = [0] * n
    cnt = 0 
    for i in range(n):
        
        if ch[i] == 0:
            Q = deque()
            ch[i] = 1
            cnt += 1    
            for j in range(n):
                if i != j and computers[i][j]==1:
                    Q.append(j)
            while Q:
                temp = Q.popleft()
                ch[temp] = 1
                for j in range(n):
                    if computers[temp][j] ==1 and temp != j  and ch[j]==0:
                        Q.append(j)
                        
                    
                    
    return cnt