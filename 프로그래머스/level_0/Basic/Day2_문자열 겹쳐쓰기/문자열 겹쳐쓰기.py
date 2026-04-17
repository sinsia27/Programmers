# def solution(my_string, overwrite_string, s):
#     return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

def solution(m, o, s):
    return m[:s]+o+m[len(o)+s:]

# s == 2
# my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
#      He       +     lloWorl      +           2+7 : 
#                                       d   <-   9 : 
#  [s:] : s 포함해서 부터 ~
#  [:s] : ~ s 바로 전 까지

# 문자열[:a] + 새문자열 + 문자열[a+b:]