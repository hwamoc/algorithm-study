def solution(answers):
    student1 = [i for i in range(1,6)] * (len(answers) //5 +1)
    student2 = [2,1,2,3,2,4,2,5] * (len(answers)//8 +1)
    student3 = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10 +1)
    score1 , score2 , score3 = 0 , 0 ,0
    for i in range(len(answers)):
        if student1[i] == answers[i]:
            score1 +=1
        if student2[i] == answers[i]:
            score2 +=1
        if student3[i] == answers[i]:
            score3 +=1    
    answer = [-1]
    answer.append(score1)
    answer.append(score2)
    answer.append(score3)
    max_ans = max(answer)
    return [i for i in range(len(answer)) if answer[i]== max_ans ]
    ####