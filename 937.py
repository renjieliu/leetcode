def reorderLogFiles(logs: 'List[str]'):
    output = []
    lst_digit=[]
    dict_letter = {}
    lst_letter_key = []
    lst_letter = []
    for i in logs :
        t = i.split(" ")
        if 97<=ord(t[1][0]) <= 122:  #the second word starts with letter
            dict_letter[" ".join(t[1:])] = t[0]
        else:
            lst_digit.append(i)

    for i in dict_letter.keys():
        lst_letter_key.append(i)

    lst_letter_key.sort()

    for i in lst_letter_key:
        lst_letter.append( dict_letter[i] + ' ' + i)


    for i in lst_letter:
        output.append(i)

    for i in lst_digit:
        output.append(i)


    return output

print(reorderLogFiles( ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
