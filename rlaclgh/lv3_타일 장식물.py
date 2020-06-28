def solution(N):
    length = [1,1]
    area = [4,6]
    for i in range(N-2):
        length.append(length[-1]+length[-2])
        area.append(area[-1]+length[-1]*2)
    return area[-1]