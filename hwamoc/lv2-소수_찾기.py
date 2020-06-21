import itertools

def solution(numbers):
    answers = []
    num = set([])

    for i in range(1, len(numbers)+1):
        p = list(itertools.permutations(numbers, i))
        for j in range(len(p)):
            s = "".join(map(str, p[j]))
            num.add(int(s))
    # print(num)
    num = list(num)
    num.sort(reverse=True)
    n = num[0]      # 최대 값을 구한다

    # 에라토스테네스의 체 (최대 값 이하에서 소수 찾기)
    a = [False, False] + [True] * (n - 1)
    primes = []     # 소수를 담는 배열 생성
    for i in range(2, n + 1):
        if a[i]:    # a[i]이 소수일 때 아래 실행 (초기에 2 들어감. 다음은 3 들어감)
            primes.append(i)    # 소수를 primes 배열에 추가
            for j in range(2 * i, n + 1, i):    # 소수의 배수들을 걸러준다. (소수의 2배수 부터 시작 n+1까지)
                a[j] = False                    # (초기에 2배수 모두 false, 다음은 3배수 false로..
    # print(primes)                             # 다음은 5, 7, 11의 배수를 false.. 계속..!)

    for s1 in num:
        if s1 in primes:
            answers.append(s1)
    print(answers)

    return len(answers)

'''
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):                                                 # for문을 돌면서
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))      # i+1개의 원소로 순열을 만든 결과를 set a와 OR연산한 뒤 결과를 a에 할당
    a -= set(range(0, 2))   # 0, 1을 세트로 만들어 빼준 결과를 다시 a에 할당

    for i in range(2, int(max(a) ** 0.5) + 1):      # 최대값의 제곱근 까지만 for문을 돈다
        a -= set(range(i * 2, max(a) + 1, i))       # 에라토스테네스의 체: 소수의 배수들을 걸러준다. 소수의 2배수 부터 시작 n+1까지
    return len(a)
'''

solution("17")
solution("011")