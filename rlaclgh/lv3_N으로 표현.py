def solution(N,number):
    total =  [[],[N]]
    for i in range(2,9):
        list = [int(str(N)*i)]
        for q in range(0,i//2):
            for x in total[q+1]:
                for y in total[i-q-1]:
                    list.append(x+y)
                    list.append(x*y)
                    list.append(x-y)
                    list.append(y-x)
                    if y != 0:
                        list.append(x//y)
                    if x != 0:
                        list.append(y//x)
        if number in list:
            return i
        total.append(list)
    return -1