def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("a"*22)
    for p,c in zip(participant,completion):
        if p != c:
            answer += p
            return answer

