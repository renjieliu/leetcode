def findKey(input: 'dict', find: 'str'):
    for k, v in input.items():
        if v==find:
            return k
    return '-1'



def findAndReplacePattern(words: 'List[str]', pattern: 'str'):
    output = []
    for w in words:
        if len(w) != len(pattern):
            continue
        else:
            map = {}
            cnt = 0
            for i in range(len(pattern)):
                if pattern[i] not in map.keys():
                    if findKey(map, w[i]) == '-1':  # pattern and target should be 1 to 1 match.
                        map[pattern[i]] = w[i]
                        cnt += 1
                else:
                    if w[i]==map[pattern[i]]:
                        cnt+=1

            if cnt == len(pattern):
                output.append(w)



    return output


print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))
print(findAndReplacePattern(["ab","cd","fe","gg"],"ab"))

