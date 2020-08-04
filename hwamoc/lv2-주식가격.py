def solution(prices):
    l = len(prices)
    count = [0 for _ in range(l)]
    for i in range(l):
        for j in range(i+1, l):
            if prices[i] <= prices[j]:
                count[i] += 1
            else:
                count[i] += 1
                break
    return count

'''
def solution(prices):
    l = len(prices)
    count = [0 for _ in range(l)]
    for i in range(l):
        for j in range(i+1, l):
            count[i] += 1
            if prices[i] > prices[j]:
                break
    return count
'''
'''
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
'''
'''
def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans
'''

print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 3, 2, 3, 1]))
print(solution([3, 1]))