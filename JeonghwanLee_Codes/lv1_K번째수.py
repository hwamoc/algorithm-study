def sort(array): #연습삼아 정렬 구현..
    print(array)
    result = [0 for i in range(len(array))]
    for i in range(len(array)):
        min=array[i]
        min_idx=i
        for j in range(i,len(array)):
            if(array[j]<min):
                min = array[j]
                min_idx=j
        
        temp = array[i]
        array[i]=array[min_idx]
        array[min_idx]=temp
    return array
        

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        result = sort(arr)
        answer.append(result[commands[i][2]-1])
    
    return answer