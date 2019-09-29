def removeDuplicates(s: str, k: int):
    stk= [{s[0]:1}]
    for i in range(1, len(s)):
        if len(stk) > 0:
            if s[i] in stk[-1]:
                if stk[-1][s[i]] +1 == k:
                    stk.pop()
                else:
                    stk[-1][s[i]] += 1
            else:
                stk.append({s[i]: 1})
        else:
            stk.append({s[i]:1})
    output = ""
    for i in stk:
        for k, v in i.items():
            output+= k*v

    return output


print(removeDuplicates(s = "abcd", k = 2))
print(removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(removeDuplicates(s = "pbbcggttciiippooaais", k = 2))