def solution(numbers):
    answer = ''
    #1차 풀이
    # numbers = sorted(numbers, key = lambda x :  (x<10 and x%10) or (x>10 and x/10),  ,reverse=True)
    numbers=sorted(map(str,numbers),key=lambda x: x*3, reverse=True)
   
    return str(int(''.join(numbers)))