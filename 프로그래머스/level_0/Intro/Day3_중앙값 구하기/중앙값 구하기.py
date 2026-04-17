def solution(array):
    array.sort() # 오름차순 정렬
    return array[(len(array) // 2)]