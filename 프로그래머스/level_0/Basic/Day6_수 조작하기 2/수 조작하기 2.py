def solution(numLog):
    answer = ''
    
    for i in range(len(numLog)-1) : 
        # 마지막 값에서 +1인 값이랑 비교해야하는데 그럼 비교할 수가 없으니까!
        diff = numLog[i+1] - numLog[i]
        if diff == 1 :
            answer += 'w'
        elif diff == -1 :
            answer += 's'
        elif diff == 10 :
            answer += 'd'
        else :
            answer += 'a'           

    return answer