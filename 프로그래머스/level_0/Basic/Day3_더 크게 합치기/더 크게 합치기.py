def solution(a, b):
    answer = 0
    num1 = f'{a}{b}'
    num2 = f'{b}{a}'
    
    if num1 >= num2 :
        answer = num1
    else :
        answer = num2
        
    return int(answer)

# return int(max(f"{a}{b}", f"{b}{a}"))