def solution(numbers, target):
    # result는 0부터 시작한다. 0, 0-a, 0+a, 0-a-b, 0-a+b, 0+a-b, 0+a+b, ...
    result = [0]

    # i는 numbers의 각 원소들
    for num in numbers:
        temp = []
        # result는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        for i in result:
            temp.append(i - num)
            temp.append(i + num)
        result = temp

    return result.count(target)

print(solution([1, 1, 1, 1, 1], 3))

'''
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''