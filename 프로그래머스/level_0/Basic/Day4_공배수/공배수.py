def solution(number, n, m):
    
    if int(number % n == 0 and  number % m == 0) :
        return 1
    else :
        return 0
    
# 왜 and 사용? 