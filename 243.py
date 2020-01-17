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
        while hmp[word1] and hmp[word2]:
            output = min(output, abs(hmp[word1][0] - hmp[word2][0]))
            if hmp[word1][0] < hmp[word2][0]:
                hmp[word1].pop(0)
            else:
                hmp[word2].pop(0)
        return output
