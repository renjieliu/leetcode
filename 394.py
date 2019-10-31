def decodeString(s: str):
    nums =  [str(_) for _ in range(10)]
    str_stk = []
    left_pos = [] #position of [
    str_pos = [] #end of string
    repeat = ""
    repeat_stk = []
    output= ""
    curr = ""
    for i in range(len(s)):
        #print(i,str_stk, repeat_stk)
        #print(s[i],str_stk)
        if s[i] in nums:
            repeat += s[i]  # if find a number
            if curr != "":
                str_stk.append(curr)
                str_pos.append(i-1)
                curr = ""
        elif s[i] == "[":
            left_pos.append(i)
            repeat_stk.append(int(repeat))  # the number should be stacked
            repeat = ""

        elif s[i] == "]":
            if len(curr) > 0:
                str_stk.append(curr)
                str_pos.append(i-1)
                curr = ""

            r = repeat_stk.pop()
            if len(repeat_stk) == 0:
                output+= r*(''.join(str_stk))
                str_stk = []
                repeat_stk = []
                left_pos = []
                str_pos = []

            else:
                x = ""
                # print(str_stk , str_pos, left_pos)
                while str_pos[-1] > left_pos[-1]:
                    x = str_stk.pop()+x
                    str_pos.pop()
                    if len(str_pos) == 0:
                        break

                x = r*x
                str_stk.append(x)
                str_pos.append(i)
                left_pos.pop()


        else: #if it's characters
            if repeat_stk ==[]:
                output+= s[i]
                curr = ""
            else:
                curr+=s[i]

    return output
#
#
print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("a3[a2[c]]"))
print(decodeString("a3[2[c]2[a]]"))
print(decodeString("3[2[c]2[a]]"))
print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")) #"zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
