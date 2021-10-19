class Solution:
    def reorganizeString(self, S: str) -> str:
        hmp =  {}
        for c in S:
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(c)
        k = sorted(hmp.keys(), key = lambda x: len(hmp[x]), reverse =  True)
        if len(hmp[k[0]]) > len(S)//2+len(S)%2: return "" # for odd length more than half+1, for even more than half
        reshuffle = []
        for i in k:
            reshuffle += hmp[i]
        first = reshuffle[:len(S)//2+len(S)%2]
        second = reshuffle[len(S)//2+len(S)%2:]
        output = ""
        while second: #the length of first >= second
            output+= first.pop(0) + second.pop(0)
        if first:
            output+=first.pop(0)
        return output
