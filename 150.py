def evalRPN(tokens: 'List[str]'):
    stk  = []
    for i in tokens:
        if i not in "+-*/":
            stk.append(i)
        else:
            if len(stk) < 2:
                return 'Error'
            else:
                a = int(stk.pop(-2))
                b = int(stk.pop(-1))
                if i =="+":
                    stk.append(int(a+b))
                elif i == "-":
                    stk.append(int(a - b))
                elif i == "*":
                    stk.append(int(a * b))
                elif i == "/":
                    stk.append(int(a / b))

    return int(stk[-1])

print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["18"]))

