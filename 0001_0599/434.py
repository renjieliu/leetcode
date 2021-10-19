def countSegments(s):
    """
    :type s: str
    :rtype: int
    """
    reg = 0
    cnt = 0
    w = 0

    s = s.strip(" ")

    for i in s:

        if i == " ":
            reg = 1

        elif i!= " " and reg == 1:
            reg = 0
            cnt +=1

        elif i!= " " and reg == 0:
            w+=1

    return cnt+1 if w!=0 else cnt

print(countSegments("Hello, my name is John"))
print(countSegments("                         "))
print(countSegments(", , , ,        a, eaefa"))
print(countSegments("Hello"))



