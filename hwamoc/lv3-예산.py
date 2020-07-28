def solution(budgets, M):
    budgets.sort()      # 예산 크기별로 정렬
    count = len(budgets)
    temp = M
    print(budgets[len(budgets)-1])

    for budget in budgets:
        if budget < temp // count :  # 예산이 평균 값보다 작으면 국가예산에서 빼고
            temp -= budget           # 도시 수에서도 -1한 뒤 다시 평균과 지방예산을 비교한다
            count -= 1
        else:
            return temp // count    # 예산이 큰 도시들의 상한액을 구한다

    return budgets[len(budgets)-1]  # 모든 지방에 예산 분배가 가능할 때 예산 금액의 최대값을 리턴한다

'''
def solution(budgets, M):
    budgets.sort()
    count = len(budgets)
    cap = 0
    for i, budget in enumerate(budgets):
        level = (budget - cap) * (count - i)
        if level <= M:
            cap = budget
            M -= level
        else:
            cap += M // (count - i)
            break
    return cap
'''

print(solution([120, 110, 140, 150], 485))
print(solution([120, 110, 100, 90], 485))