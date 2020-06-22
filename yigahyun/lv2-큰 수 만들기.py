def solution(number, k):
    num = list(number)
    num_list = [num[0]]
    i = 1
    answer = ''
    cnt = 0
    while i < len(num):
        if num[i-1] < num[i] and cnt < k: # 전의 수보다 현재 수가 더 크다면
            num_list[-1] = num[i] # 현재 수 추가
            cnt += 1 # 제거한 수의 갯수 + 1
            for j in range(len(num_list)-1, 0,-1):# 추가 한 수보다 작은 수가 있다면
                if num_list[j] > num_list[j-1] and cnt < k:
                    del num_list[j-1]  # 삭제
                    cnt += 1  # 제거한 수 의 갯수 +1
                else:
                    break
        else: # 전의 수가 더 크다면
            num_list.append(num[i])
        i += 1

    for i in range(len(number)-k):
        answer += num_list[i]
    return answer