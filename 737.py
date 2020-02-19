class Solution:
    def areSentencesSimilarTwo(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        def root(curr, hmp):  # this is to find the root of curr in hmp
            if curr not in hmp:
                hmp[curr] = curr
            while hmp[curr] != curr:
                curr = hmp[curr]
            return curr

        hmp = {}
        i = 0
        while i < len(pairs):
            a = root(pairs[i][0], hmp)
            b = root(pairs[i][1], hmp)
            hmp[a] = b
            i += 1

        if len(words1) != len(words2):
            return False
        i = 0
        while i < len(words1):
            if root(words1[i], hmp) != root(words2[i], hmp):
                return False
            i += 1
        return True

