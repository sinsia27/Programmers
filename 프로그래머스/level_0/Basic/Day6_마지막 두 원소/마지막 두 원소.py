def solution(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    
    if n1 > n2 :
        num_list.append(n1-n2)
    else :
        num_list.append(n1*2)

#     n = len(num_list)
    
#     if num_list[n-1] > num_list[n-2] :
#         num_list.append(num_list[n-1] - num_list[n-2])
#     else :
#         num_list.append(num_list[n-1]*2)
    
    return num_list