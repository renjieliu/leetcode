class Solution:
    def findLUSlength(self, strs: 'List[str]') -> int:
        def isCommon(a, b): #len(a) >= len(b)
            a = list(a)
            b = list(b)
            while a and b:
                if a[0] == b[0]:
                    a.pop(0)
                    b.pop(0)
                else:
                    a.pop(0)
            return b == []

        hmp = defaultdict(lambda:0)
        for s in strs:
            hmp[s] += 1
        strs.sort()
        strs.sort(key = lambda x: len(x),reverse = True)
        output = -float('inf')
        carry = 0 # to show the previous str is common with the prevprev str
        for i in range(1, len(strs)):
            if len(strs[i-1]) > len(strs[i]):
                if carry == 0:
                    return len(strs[i-1])
            if strs[i] != strs[i-1]:
                if isCommon(strs[i-1], strs[i]) == False:
                    if carry == 0:
                        return len(strs[i-1])
                    else:
                        if hmp[strs[i]] == 1:
                            cnt = 0
                            for s in strs: # current str need to be uncommon with all others.
                                if isCommon(s,strs[i]) == False:
                                    cnt += 1
                            if cnt == len(strs)-1:
                                return len(strs[i])
                else:
                    carry = 1
            else:
                carry = 1
        return -1






