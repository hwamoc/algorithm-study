def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []      # 수포자들의 정답수를 count하는 배열

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:   # 수포자들의 답안 인덱스: 정답의 인덱스를 수포자 답안의 순환주기로 나눈 나머지
            score[0] += 1                           # 수포자의 답과 정답을 비교, 정답일 경우 해당 수포자에 정답수 +1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):     # 가장 많이 정답을 맞춘 사람 인덱스를 리턴
            result.append(idx+1)

    return result

# def solution(answers):
#     supo = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     right = [0] * len(supo)     # 수포자들의 정답수를 count하는 배열
#
#     for q, answer in enumerate(answers):
#         for i, mark in enumerate(supo):
#             if answer == mark[q % len(mark)]:     # 수포자들의 답안 인덱스: 정답의 인덱스를 순환주기로 나눈 나머지
#                 right[i] += 1                     # 수포자의 답과 정답을 비교, 정답일 경우 해당 수포자의 인덱스에 정답수 +1
#     return [i + 1 for i, v in enumerate(right) if v == max(right)]      # 가장 많이 정답을 맞춘 사람 인덱스를 리턴

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

