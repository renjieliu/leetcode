def reverseParentheses(s: str):
    output = ""
    curr = []
    stk = 0

    for i in range(len(s)):
        t = s[i]
        if t == "(":
            stk += 1
            curr.append("")
        else:
            if stk == 0:
                output += t
            else:
                if t != ")":
                    curr[-1] += t
                else:
                    stk -= 1
                    temp = curr[-1][::-1]
                    curr = curr[:-1]
                    if stk == 0:
                        output += temp
                    else:
                        curr[-1] += temp

    return output


print(reverseParentheses("(abcd)"))
print(reverseParentheses("asd()"))
print(reverseParentheses("(u(love)i)"))
print(reverseParentheses("abc(def)g(hi)gj"))
print(reverseParentheses( s = "(ed(et(oc))el)"))
print(reverseParentheses( s = "a(bcdefghijkl(mno)p)q")) #apmnolkjihgfedcbq
