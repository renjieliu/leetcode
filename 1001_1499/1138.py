def alphabetBoardPath(target: str) :
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    walk = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            walk[board[i][j]] = [i, j]

    output = ""
    prev = "a"
    currPos = [0,0]
    for i in target:
        str1 = ""
        str2 = ""
        if i == prev:
            output += '!'

        elif i =='z': #only from 'u' down 1 can reach 'z'
            if walk['u'][0] - currPos[0] > 0:
                str1 = "D" * (walk['u'][0] - currPos[0])
            else:
                str1 = "U" * (currPos[0] - walk['u'][0])

            if walk['u'][1] - currPos[1] > 0:
                str2 = "R" * (walk['u'][1] - currPos[1])
            else:
                str2 = "L" * (currPos[1] - walk['u'][1])


            output += str1 + str2 + "D!"
            currPos = walk[i]


        else:
            if walk[i][0] - currPos[0] >0:
                str1 = "D" * (walk[i][0] - currPos[0])
            else:
                str1 = "U" * (currPos[0] - walk[i][0] )

            if walk[i][1] - currPos[1]>0:
                str2 = "R" * (walk[i][1] - currPos[1])
            else:
                str2 = "L" * (currPos[1]-walk[i][1])

            output+= str1+ str2 + "!"
            currPos = walk[i]
        prev = i
    return output



print(alphabetBoardPath("az"))
print(alphabetBoardPath("dz"))
print(alphabetBoardPath("zdzz")) #"DDDDD!UUUUURRR!DDDDLLLD!" #DDDDD!UUUUURRR!DDDDDLLL!
print(alphabetBoardPath("leet")) #"DDR!UURRR!!DDD!"
print(alphabetBoardPath("code")) #"RR!DDRR!UUL!R!"