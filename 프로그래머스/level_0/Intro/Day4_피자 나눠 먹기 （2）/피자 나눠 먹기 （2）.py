def solution(n):
    pizza = 1
    
    while (pizza * 6) % n != 0:
        pizza += 1
    
    return pizza

# 반복 횟수 정해짐	for
# 언제 끝날지 모름	while