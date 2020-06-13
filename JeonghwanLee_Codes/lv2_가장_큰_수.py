def solution(numbers):
    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number))
    #number를 str형태로
    
    equalized_number = []
    
    for number in str_numbers:
        temp_number = number
        number_length = len(number)
        for _ in range(4):
        #4번 반복한다음 잘라서 원본 자릿수와 저장
        #6,10,2 -> 6666,10101010,2222 -> [[6666,1],[1010,2][2222,1]]
            temp_number+=number
        equalized_number.append([int(temp_number[:4]),number_length])
    
    #만든 숫자 기준으로 정렬(2차 기준은 자릿수가 작은 순)
    sorted_number = sorted(equalized_number,key=lambda x:(-x[0],x[1]))
    result = ""
    for number in sorted_number:
        #원본 자릿수만큼만 자른 후 차례대로 답에 붙임 
        result+=str(number[0])[:number[1]]
    return str(int(result))#[0,0,0,0] case 때문에..