def solution(array, commands):
    answer = []
    #1차 풀이
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return answer