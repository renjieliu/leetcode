class Solution:
    def makeEqual(self, words: 'List[str]') -> bool:
        hmp = defaultdict(lambda: 0)
        for w in words:
            for c in w:
                hmp[c] += 1
        for v in hmp.values():
            if v%len(words)!=0:
                return False
        return True

