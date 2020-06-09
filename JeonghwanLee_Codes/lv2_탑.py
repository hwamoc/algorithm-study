def solution(heights):
    reversed_answer = []
    reversed_heights = list(reversed(heights))
    for i,elem in enumerate(reversed_heights):
        flag = True
        for j in range(i,len(reversed_heights)):
            if flag is False:
                break
            if elem < reversed_heights[j]:
                reversed_answer.append(len(heights)-j)
                flag = False
        if flag is True:
            reversed_answer.append(0)
    answer = list(reversed(reversed_answer))
    return answer