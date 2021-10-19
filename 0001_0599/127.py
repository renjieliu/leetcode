class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        if endWord not in wordList: return 0
        hmp = {}
        for w in wordList:
            for i in range(len(w)): #all the possible candidates
                if w[:i] + '*' + w[i+1:] not in hmp:
                    hmp[w[:i] + '*' + w[i+1:]] = []
                hmp[w[:i] + '*' + w[i+1:]].append(w)

        layer = 1
        stk = [beginWord]
        run = 1
        while run == 1 :
            nxt = []
            while stk:
                curr = stk.pop(0)
                if curr == endWord:
                    return layer
                for i in range(len(curr)):
                    mask = curr[:i] + '*' + curr[i+1:] #all the possible candidates derived from current word
                    if mask in hmp:
                        nxt += hmp[mask] # next round of check
                        del hmp[mask]
            layer += 1
            stk = nxt
            if stk == []:
                run = 0

        return 0
