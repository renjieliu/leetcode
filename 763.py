def partitionLabels(S: str):
    map = {}
    temp = [0]

    for i in range(len(S)):
        if S[i] not in map.keys() :
            map[S[i]] = []
            map[S[i]].append(i)
        else:
            map[S[i]].append(i)
    #print(map)
    splitEnd = map[S[0]][-1]

    for i in range(len(S)):
        if map[S[i]][-1]>splitEnd :
            if map[S[i]][0] <= splitEnd: #or len(map[S[i]]) == 1:
                splitEnd = map[S[i]][-1]
            else:
                temp.append(splitEnd+1) #+1 for the next start, makes it easier to compute the size of the array
                splitEnd = map[S[i]][-1]

    temp.append(len(S)) # the last split point
    # print(temp)
    output = []

    for i in range(1, len(temp)):
        output.append(temp[i]- temp[i-1])

    return output


print(partitionLabels("ababcbacadefegdehijhklij"))
print(partitionLabels("a"))
print(partitionLabels("aaaabab"))
print(partitionLabels("eaaaabaaec"))
