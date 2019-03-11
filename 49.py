def signature(input):
    output = ""
    map = {}
    for i in input:
        if i in map:
            map[i] +=1
        else:
            map[i] =1
    temp = []
    for k, v in map.items():
        temp.append(k)
    temp.sort()

    for i in temp:
        output += i+str(map[i])

    return output


def groupAnagrams(strs: 'List[str]'):
    map = {}
    for i in strs :
        t = signature(i)
        if t not in map:
            map[t] = []
        map[t].append(i)

    return list(map.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



