def minAddToMakeValid(S: str):
    left_cnt = 0
    right_cnt = 0
    for i in S:
        if i=="(":
            left_cnt+=1
        else:
            if left_cnt >= 1:
                left_cnt-=1
            else:
                right_cnt +=1
    return right_cnt+left_cnt




print(minAddToMakeValid("())"))
print(minAddToMakeValid("((("))
print(minAddToMakeValid("()"))
print(minAddToMakeValid(")))((("))
print(minAddToMakeValid("()))(("))