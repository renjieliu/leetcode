def isLongPressedName(name: 'str', typed: 'str'): #ALEX --> A1L1E1X1, ALLEXX -->A1L2E1X2  --> so, the second string is long pressed.
    N1 = []
    N2 = []

    curr = 0
    N1.append(name[0])
    N2.append(1)
    for i in range(1, len(name)):
        if name[i] == name[i-1]:
            N2[curr] += 1
        else:
            curr += 1
            N1.append(name[i])
            N2.append(1)

    N3 = []
    N4 = []

    curr = 0
    N3.append(typed[0])
    N4.append(1)
    for i in range(1, len(typed)):
        if typed[i] == typed[i - 1]:
            N4[curr] += 1
        else:
            curr += 1
            N3.append(typed[i])
            N4.append(1)

    if len(N1) != len(N3):
        return False

    for i in range(0, len(N1)):
        if N1[i]!=N3[i] or N2[i]>N4[i]:
            return False

    return True


print(isLongPressedName("alex", "aaleex"))
print(isLongPressedName("saeed", "ssaaedd"))
print(isLongPressedName("leelee", "lleeelee"))
print(isLongPressedName("pyplrz", "ppyypllr"))


