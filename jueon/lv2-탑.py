def solution(heights):
    answer = [0]*len(heights)
    #리스트를 이용한 풀이
    # if len(heights)>0:
    #     for j in range(len(heights)-1, 0, -1):
    #         for i in range(j-1,-1,-1):
    #             if heights[j]<heights[i] and answer[j]==0:
    #                 answer[j]=i+1
    #                 break
    
    #스택을 이용한 풀이
    while heights: #스택에 값이 남아있나를 확인한다.
        j=heights.pop() #남아있을 경우 pop 연산 수행
        for i in range(len(heights)-1,-1,-1): #heights를 거꾸로 돌려 pop값과 비교한다.
            if heights[i]>j:
                answer[len(heights)]=i+1
                break
        
    return answer