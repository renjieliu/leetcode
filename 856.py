def scoreOfParentheses( S: str):
    calc_stk = []
    left_pos = []
    calc_stk_pos = []
    for i in range(len(S)):
        t = S[i]
        if t == "(":
            left_pos.append(i) #add current loc to the stack
        elif t == ")":
            if left_pos[-1] == i-1: #the last "(" is right before the curr ")"
                calc_stk.append(1)
                calc_stk_pos.append(i)
                left_pos.pop()
            else:
                #find all the stk[x] between last ( and current i
                x = 0
                while calc_stk_pos[-1] > left_pos[-1]:
                    x+=calc_stk[-1]
                    calc_stk_pos.pop()
                    calc_stk.pop()
                    if len(calc_stk_pos) * len(left_pos) ==  0:
                        break

                left_pos.pop()
                calc_stk.append(2*x)
                calc_stk_pos.append(i)


    return sum(calc_stk)

#
print(scoreOfParentheses("()"))
print(scoreOfParentheses("(()())"))
print(scoreOfParentheses("()()"))
print(scoreOfParentheses("(()())()(())()"))
print(scoreOfParentheses("((()()((()()))))()(())(())(())((()))")) #40
