class Solution:
    def areSentencesSimilar(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2 ):
            return False
        else:
            tmp = pairs.copy()
            for p in pairs:
                tmp.append(p[::-1])
            hmp = {}
            for t in tmp:
                if t[0] not in hmp:
                    hmp[t[0]] = [t[0]] #add itself
                hmp[t[0]].append(t[1]) #add the similar one
            i = 0
            while i < len(words1):
                if (words2[i] not in hmp or words1[i] not in hmp[words2[i]]) and words1[i] != words2[i]:
                    return False
                i+=1
            return True