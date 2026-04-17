def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr

# 동시 할당 (swap) 문법
# a, b = b, a