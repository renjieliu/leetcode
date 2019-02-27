def findJudge(N: 'int', trust: 'List[List[int]]'):
    if N == 1 and len(trust) == 0:
        return 1


    dict = {}
    max = 0
    for i in trust:
        if i[1] not in dict.keys():
            dict[i[1]] = 1
        else:
            dict[i[1]] +=1

        if dict[i[1]] > max:
            max = dict[i[1]]

    if max != N-1:
        return -1
    else:
        output = []
        for k,v in dict.items():
            if v==max:
                output.append(k)

        if len(output) != 1 :
            return -1


    for i in trust:
        if i[0]==output[0]:
            return -1

    return output[0]


print(findJudge(2, [[1,2]]))
print(findJudge(3, [[1,3],[2,3]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))
print(findJudge(3, [[1,2],[2,3]]))
print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(findJudge(1, [])) #the judge does not trust any one, and every one else trusts the judge


