def solution(answers):
    answer = []
    total = len(answers)
    a = total // 5
    b = total % 5
    arr = [1, 2, 3, 4, 5]
    p1 = arr * a
    for i in range(b):
        p1.append(arr[i])

    a = total // 8
    b = total % 8
    arr = [2, 1, 2, 3, 2, 4, 2, 5]
    p2 = arr * a
    for i in range(b):
        p2.append(arr[i])

    a = total // 10
    b = total % 10
    arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p3 = arr * a
    for i in range(b):
        p3.append(arr[i])

    result = [0, 0, 0]

    for i in range(total):
        if p1[i] == answers[i]:
            result[0] += 1
        if p2[i] == answers[i]:
            result[1] += 1
        if p3[i] == answers[i]:
            result[2] += 1

    answer.append(1)
    max_v = result[0]
    for i in range(1,3):
        if result[i] > max_v:
            max_v = result[i]
            answer = [i+1]
        elif result[i] == max_v:
            answer.append(i+1)
    return answer


print(solution([1,3,2,4,2]))
