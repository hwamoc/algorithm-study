def solution(N):
    fibonacci = [0 for _ in range(N+1)]
    fibonacci[0] = fibonacci[1] = 1

    for i in range(2, N+1):
        fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[-1] * 2 + fibonacci[-2] * 2

print(solution(5))
print(solution(6))

'''
def solution(N):
    a, b = 1, 1
    while N+2 > 2:
        a, b = b, a + b
        N -= 1
    return 2 * b
'''