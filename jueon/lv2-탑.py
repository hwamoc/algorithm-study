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
    while heights:
        j=heights.pop()
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>j:
                answer[len(heights)]=i+1
                break
        
    return answer