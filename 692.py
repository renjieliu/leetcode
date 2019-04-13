def topKFrequent( words: 'List[str]', k: int):
    map = {}
    for i in words:
        if i not in map:
            map[i]= 0
        map[i] +=1

    values = []
    for key,v in map.items():
        values.append(v)
    values.sort(reverse=1)
    cnt = 0
    output = []
    while cnt < k:
        t = []
        for key, v in map.items():
            if v==values[cnt] and key not in output:
                t.append(key)
        curr = 0
        for j in sorted(t):
            output.append(j)
            curr+= 1
            if len(output) ==k:
                return output
        cnt += curr
    return output

print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
print(topKFrequent( ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
print(topKFrequent( ["i", "love", "leetcode", "i", "love", "coding"], 3)) # ["i","love","coding"]