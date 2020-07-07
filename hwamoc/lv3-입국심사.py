def solution(n, times):
  left, right = 1, max(times) * n   # 최악의 경우: 모든 심사관에게 받는 경우의 시간.
  answer = 0
  while left <= right:
    mid = (left + right) // 2   # 한 심사관에게 주어진 시간
    people = 0
    for i in times:
      people += mid // i  # 각 심사관마다, 주어진 시간 동안 몇 명의 사람을 심사할 수 있는지
      if people >= n:     # 모든 사람을 심사할 수 있으면 시간을 줄여본다
        answer = mid
        right = mid - 1
        break
    if people < n:    # 모든 사람을 심사할 수 없는 경우
      left = mid + 1  # 한 심사관에게 주어진 시간을 늘려본다.
  return answer

print(solution(6, [7, 10]))

'''
def solution(n, times):
    answer = 0
    mintime = int(min(times) * n / len(times))
    maxtime = int(max(times) * n / len(times))
    while mintime != maxtime:
        target_time = (mintime + maxtime) // 2
        pass_num = sum([target_time // time for time in times]) - n
        print('min {}, target {}, max {}, pass {}'.format(mintime, target_time, maxtime, pass_num))
        if pass_num >= 0:
            maxtime = target_time
        if pass_num < 0:
            mintime = target_time
        if maxtime - mintime == 1:
            break
    return maxtime
'''