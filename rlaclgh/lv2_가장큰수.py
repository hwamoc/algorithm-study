def solution(numbers):
    numbers.sort(key = lambda x: (str(x)[0],str(x)*3),reverse = True)
    numbers_str = [str(x) for x in numbers]
    return str(int(''.join(numbers_str)))