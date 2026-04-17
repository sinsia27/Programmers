def solution(a, b):
    answer = 0
    num1 = f'{a}{b}'
    num2 = 2 * a * b
    
    if int(num1) >= num2 :
        answer = num1
    else :
        answer = num2
    return int(answer)