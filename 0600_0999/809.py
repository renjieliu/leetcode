def signature(inp):
    if len(inp) ==0:
        return []
    curr = inp[0]
    sig = ""
    cnt = 1
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            cnt +=1
        else:
            sig+=curr + " "+ str(cnt) + ","
            cnt = 1
            curr = inp[i]

    sig+= curr + " "+ str(cnt)  #to add the last character

    return sig.split(',')


def expressiveWords(S: str, words: 'List[str]'):
    if len(S) ==0 or len(words) ==0:
        return 0

    ref = signature(S)
    cnt  = 0
    for j in words:
        curr = signature(j)
        if len(curr) != len(ref):
            continue
        else:
            good = 1
            for k in range(len(curr)):
                if curr[k].split(' ')[0] != ref[k].split(' ')[0]:
                    good =0
                    break
                else:
                    ref_cnt = int(ref[k].split(' ')[1])
                    curr_cnt = int(curr[k].split(' ')[1])
                    if ref_cnt < curr_cnt:
                        good = 0
                        break
                    else:
                        if ref_cnt > curr_cnt and ref_cnt < 3:
                            good = 0
                            break

            if good ==1:
                cnt +=1

    return cnt

print(expressiveWords("heeellooo",  ["hello", "hi", "helo", "heeellooo"]))
print(expressiveWords("heeellooo",  []))
print(expressiveWords("sfasf",  ["","s"]))

