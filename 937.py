def reorderLogFiles(logs: 'List[str]'):
    lst_digit = []
    dict_letter = {}
    lst_letter = []
    for i in logs:
        t = i.split(" ")
        if 97 <= ord(t[1][0]) <= 122:  # the second word starts with letter
            dict_letter[" ".join(t[1:])] = t[0]
        else:
            lst_digit.append(i)

    for i in dict_letter.keys():
        lst_letter.append(i)

    lst_letter.sort()

    for i in range(len(lst_letter)):
        lst_letter[i] = dict_letter[lst_letter[i]] + ' ' + lst_letter[i]

    return lst_letter + lst_digit

print(reorderLogFiles( ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
