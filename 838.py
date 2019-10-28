def pushDominoes(dominoes: str):
    if len(dominoes) < 2:
        return dominoes
    output = ""
    r_cnt = -1
    lkp = []
    for i in dominoes:
        if i == "R":
            lkp.append(['R', 'R'])
            r_cnt = 0
        elif i == "L":
            lkp.append(['L', 'L'])
            r_cnt = -1
        elif i == ".":
            if r_cnt != -1:
                r_cnt += 1
                lkp.append([0, r_cnt])
            else:
                lkp.append([0, 0])

    l_cnt = -1
    for i in range(len(dominoes) - 1, -1, -1):
        if dominoes[i] == "R":
            l_cnt = -1
        elif dominoes[i] == "L":
            l_cnt = 0
        elif dominoes[i] == ".":
            if l_cnt != -1:
                l_cnt += 1
                lkp[i][0] = l_cnt

    for i in range(len(lkp)):
        if dominoes[i] in ['R', 'L']:
            output += dominoes[i]
        else:
            if lkp[i][0] == lkp[i][1] == 0:
                output += "."
            elif lkp[i][0] == 0:
                output += "R"
            elif lkp[i][1] == 0:
                output += 'L'
            else:
                x = lkp[i][0] - lkp[i][1]  # rightDist - leftDist
                if x == 0:
                    output += "."
                elif x > 0:
                    output += "R"
                else:
                    output += "L"

    return output


print(pushDominoes(".L.R...LR..L.."))
print(pushDominoes("RR.L"))
