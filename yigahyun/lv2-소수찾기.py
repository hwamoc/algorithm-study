from itertools import permutations
def check(n): # 소수 판별
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
    return True


def solution(numbers):
    answer = 0
    # 숫자 조합
    for i in range(1,len(numbers)+1):
        num_list = permutations(list(numbers),i)
        for num in set(num_list):
            if num[0] != '0':
                n = ''.join(list(num))
                if check(int(n)):
                    answer += 1
    return answer


print(solution("17"))

