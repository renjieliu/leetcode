def shortestCompletingWord(licensePlate: 'str', words: 'List[str]'):
    compare  = ""
    output = ""
    min_size = float('inf')
    for i in licensePlate: #this is to remove the non letter part of the plate
        if 65<=ord(i)<=90 or 97<=ord(i) <= 122:
            compare += i.lower()

    for w in words:
        t = str(w)
        cnt = 0
        for c in compare:
            if t.find(c) == -1:
                break
            else:
               cnt +=1
               t = t.replace(c,"",1)

        if cnt==len(compare) and len(w) < min_size:
            min_size = len(w)
            output = w

    return output


print(shortestCompletingWord("1s3 PSt"  , ["step", "steps", "stripe", "stepple"]))
