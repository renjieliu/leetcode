def numEquivDominoPairs(dominoes: 'List[List[int]]'):
    def fact(n):
        output = 1
        for i in range(1, n + 1):
            output *= i
        return output

    newDominos = []
    for i in dominoes:
        t = sorted(i)
        newDominos.append( str(t[0]) + '-' + str(t[1]))

    dict = {}
    for i in newDominos:
        if i not in dict:
            dict[i] = 0
        dict[i]+=1

    output =0

    for k, v in dict.items():
        if v>1:
            output += fact(v)/(fact(v-2)*2)

    return  int(output)


print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
print(numEquivDominoPairs([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]))



