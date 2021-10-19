def numSmallerByFrequency(queries: 'List[str]', words: 'List[str]'):
    def f(s):
        minn = "z"
        res = 0
        for i in s:
            if i == minn:
                res+=1
            elif i < minn:
                minn = i
                res = 1
        return res

    output = []
    t1 = []
    t2 = []
    for i in queries:
        t1.append(f(i))
    for i in words:
        t2.append(f(i))
    t2.sort()
    l = len(t2)
    for i in t1:
        cnt = 0
        find =0
        for j in range(l):
            if t2[j] > i:
                output.append(l-j)
                find =1
                break

        if find == 0:
            output.append(cnt)

    return output

print(numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
print(numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))

