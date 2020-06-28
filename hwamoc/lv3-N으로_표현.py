def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        numbers = set()     # set 초기화
        numbers.add(int(str(N) * i))    # set마다 기본 수 "N" * i 수 초기화
        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)
        if number in numbers:
            answer = i
            break

        dp.append(numbers)

    return answer

print(solution(5, 12))
print(solution(2, 11))
print(solution(5, 31168))