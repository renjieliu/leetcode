class Solution:
    def shortestDistance(self, words: 'List[str]', word1: str, word2: str) -> int:
        hmp = {}
        i = 0
        while i < len(words):
            if words[i] not in hmp:
                hmp[words[i]] = []
            hmp[words[i]].append(i)
            i += 1
        output = float('inf')
        for x in hmp[word1]:
            for y in hmp[word2]:
                output = min(output, abs(x - y))
        return output
