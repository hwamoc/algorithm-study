
def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 문자열 비교는 맨앞의 문자부터 비교함.
    # 3 > 330 이려면 333 > 330 (3을 곱해서 자리맞춰준다.)

    answer = str(int(''.join(numbers)))
    return answer
print(solution([3, 30, 34, 5, 9]))