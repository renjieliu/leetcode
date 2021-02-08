def maxProduct(words: 'List[str]'):
    output = 0

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            s1 = words[i]
            s2 = words[j]
            if len(set(s1) | set(s2)) == len(set(s1))+ len(set(s2)):
                output = max(len(words[i])*len(words[j]), output)

    return  output


print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(maxProduct(["a","aa","aaa","aaaa"]))
print(maxProduct(["a"]))
print(maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))