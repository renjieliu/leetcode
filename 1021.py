def removeOuterParentheses(S: str) -> str:
    cnt_left = 0
    cnt_right = 0
    output = ""
    temp = ""
    for i in S:
        if i =="(":
            cnt_left +=1
        else:
            cnt_right +=1
        temp+=i
        if cnt_left ==cnt_right:
            output+= temp[1:-1]
            temp = ""
            cnt_left = 0
            cnt_right = 0

    return output




print(removeOuterParentheses("(()())(())"))
print(removeOuterParentheses("(()())(())(()(()))"))
print(removeOuterParentheses("()()"))



