class Solution:
    def beautySum(self, s: str) -> int:
        def calc(s):
            hmp = defaultdict(int)
            for c in s :
                hmp[c]+=1
            return max(hmp.values()) - min(hmp.values())
        pool = []
        output = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                pool.append(s[i:j])
        for p in pool:
            output += calc(p)
        return output

