def solution(number, k):
    stack = []     # 1. 스택 생성

    for elem in number:     # 2. 큰 수가 앞자리가 되게끔 스택에 저장합니다.
        while stack and stack[-1] < elem and k > 0:
            stack.pop()
            k -= 1

        stack.append(elem)

    while k > 0:    # 3. k가 남았다면 뒤에서부터 뺍니다.
        stack.pop()
        k-=1

    answer = "".join(stack)
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
