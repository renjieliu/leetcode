class WordDistance:

    def __init__(self, words: 'List[str]'):
        self.hmp = {}
        i = 0
        while i < len(words):
            if words[i] not in self.hmp:
                self.hmp[words[i]] = []
            self.hmp[words[i]].append(i)
            i += 1

    def shortest(self, word1: str, word2: str) -> int:
        output = float('inf')
        if self.hmp[word1][0] > self.hmp[word2][-1]:  # no overlap
            return abs(self.hmp[word1][0] - self.hmp[word2][-1])
        elif self.hmp[word2][0] > self.hmp[word1][-1]:
            return abs(self.hmp[word1][-1] - self.hmp[word2][0])  # no overlap
        else:
            stop = 0
            for x in self.hmp[word1]:
                j = stop
                while j < len(self.hmp[word2]):
                    y = self.hmp[word2][j]
                    output = min(output, abs(x - y))
                    if output == 1 or (
                            y > x and x == self.hmp[word1][-1]):  # the next y will be further, no need to iterate
                        return output
                    elif y > x:
                        stop = j  # stop here, and next check should begin here.
                        break
                    j += 1
        return output

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)