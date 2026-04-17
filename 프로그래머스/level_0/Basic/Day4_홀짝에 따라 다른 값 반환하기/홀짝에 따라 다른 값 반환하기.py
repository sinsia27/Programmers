def solution(n):
    answer = 0
    
    if n % 2 : # 홀수일 경우 ? 1이 참이니까
        for i in range(1,n+1,2):
            answer += i
    else :
        for i in range(2,n+1,2):
            answer += i**2
    
    return answer
