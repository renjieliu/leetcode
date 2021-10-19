class Solution:
    def numOfPairs(self, nums: 'List[str]', target: str) -> int:
        fact = lambda x: 1 if x == 0 or x == 1 else x * fact(x-1)
        perm = lambda x, y: fact(x) // (fact(x-y))
        output = 0
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] += 1
        for k in hmp.keys():
            if k == target[-len(k):]: #current word is matching with second half the target
                pre = target[:-len(k)]
                if pre == k:
                    if hmp[pre] > 1:
                        output += perm(hmp[pre],2)
                else:
                    if pre in hmp:
                        output += hmp[pre] * hmp[k]
        return output


