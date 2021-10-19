def balancedStringSplit(s: str):
    output = 0
    l_cnt = 0
    r_cnt = 0
    for i in s:
        if i == "R":
            r_cnt += 1
        else:
            l_cnt += 1

        if l_cnt== r_cnt:
            output += 1
            l_cnt = 0
            r_cnt =0

    return output



print(balancedStringSplit("RLRRLLRLRL")) #4
print(balancedStringSplit("RLLLLRRRLR")) #3
print(balancedStringSplit("LLLLRRRR")) #1
print(balancedStringSplit("L"))#0
print(balancedStringSplit("RRLRRLRLLLRL")) #2

