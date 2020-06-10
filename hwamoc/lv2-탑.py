def solution(heights):
    stack = []
    answer = [0] * len(heights)

    for h in heights:
        stack.append(h)

    while stack:
        top = stack.pop()
        for i in range(len(stack)-1, -1, -1):
            if top < stack[i]:
                answer[len(stack)] = i+1
                break

    return answer

print(solution([6, 9, 5, 7, 4]))
print(solution([3, 9, 9, 3, 5, 7, 2]))
print(solution([1, 5, 3, 6, 7, 6, 5]))