def findReplaceString(S: str, indexes: 'List[int]', sources: 'List[str]', targets: 'List[str]'):
    if len(indexes ) ==0:
        return S


    temp = ""
    index_cp = indexes.copy()

    for i in range(len(indexes)):
        length = len(sources[i])
        if S[indexes[i]:indexes[i]+length] != sources[i]:
            index_cp[i] = -1

    i=0
    while i <len(S):
        if i not in index_cp:
            temp+=S[i]
            i+=1
        else:
            pos = index_cp.index(i)
            temp+=targets[pos]
            replaceLength = len(sources[pos])
            i+=replaceLength

    return temp





print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]))
print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]))


