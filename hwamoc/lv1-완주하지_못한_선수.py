def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    completion.append("")

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer

# 파사기당~~~~
# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))