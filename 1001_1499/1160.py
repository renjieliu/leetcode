def countCharacters(words: 'List[str]', chars: str):
    if len(chars)==0:
        return 0
    dic_ref  = {}
    for i in chars:
        if i not in dic_ref:
            dic_ref[i] =0
        dic_ref[i] += 1
    output = ""
    for i in words:
        good = 1
        dic_curr = {}
        for j in i:
            if j not in dic_curr:
                dic_curr[j] = 0
            dic_curr[j] += 1

        for k,v in dic_curr.items():
            if k not in dic_ref or v > dic_ref[k]:
                good = 0
                break

        if good==1:
            output+=i

    return len(output)

print(countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
print(countCharacters(words = ["",""], chars = ""))

