def solution(n, lost, reserve):
    students = [1] * n      # 학생 수만큼 배열을 만들어준다 (배열의 값 1은 체육복 가지고 있다는 것을 의미한다)

    for i in lost:      # 체육복 없는 학생의 인덱스에는 -1 해준다 (하나도 없는 학생은 0이 된다)
        students[i-1] -= 1

    for i in reserve:       # 여벌의 체육복을 가져온 학생의 인덱스에는 +1 해준다
        students[i-1] += 1  #(여벌의 체육복이 있고 도둑맞지 않은 학생은 2가 된다)

    for i, v in enumerate(students):    # index와 학생이 가지고 있는 체육복 갯수를 enumerate를 사용해 tuple형태로 반환
        if v == 0:      # 체육복을 도난당한 학생일 때
            if i > 0 and students[i-1] == 2:    # 앞 번호의 학생이 여벌을 가지고 있으면
                students[i-1] -= 1              # 앞 번호 학생에게 빌려서 (앞 번호 학생 값에 -1 해준다)
                students[i] += 1                # 입는다 (도난 당한 학생 값에 +1 해준다)
            elif i < n-1 and students[i+1] == 2:    # 뒷 번호의 학생이 여벌을 가지고 있으면
                students[i+1] -= 1                  # 뒷 번호 학생에게 빌려서 (뒷 번호 학생 값에 -1) 입는다 (도난 당한 학생 값에 +1)
                students[i] += 1                    # index 에러 주의: 뒤에 있는 학생 인덱스를 비교하므로 i는 n-1 보다 작은 수여야 함
    return len(students) - students.count(0)    # 체육복이 없는 (값이 0) 학생 수를 빼서 체육 수업 할 수 있는 학생 수를 반환


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))