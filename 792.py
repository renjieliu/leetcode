def numMatchingSubseq(S: str, words: 'List[str]'):
    cnt = 0
    for i in words:
        t = S
        ok = 0
        for w in i:
            if t.find(w) == -1:
                break
            else:
                t = t[t.index(w) + 1:]
                ok += 1

        if ok == len(i):
            cnt += 1

    return cnt


print(numMatchingSubseq("abcde",  ["a", "bb", "acd", "ace"]))