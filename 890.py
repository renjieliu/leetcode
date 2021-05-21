class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: str) -> 'List[str]':
        output = []
        for w in words:  #if str a --> pattern b, pattern b --> str a
            hmp_a = {} #from string, map to pattern
            hmp_b = {} #from pattern, map to string
            good = 1
            for i in range(len(w)):
                if pattern[i] not in hmp_a and w[i] not in hmp_b:
                    hmp_a[pattern[i]] = w[i]
                    hmp_b[w[i]] = hmp_a[pattern[i]]
                elif pattern[i] not in hmp_a or w[i] not in hmp_b or hmp_a[pattern[i]] != w[i] or hmp_b[w[i]] != hmp_a[pattern[i]]:
                    good = 0
                    break
            if good == 1:
                output.append(w)
        return output


