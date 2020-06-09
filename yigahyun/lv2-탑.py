def solution(heights):
    answer = []
    while heights:
        index = 0
        sending = heights.pop()
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > sending:
                index = i+1
                break
        answer.insert(0,index)

    return answer

