class Solution:
    def beautySum(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            hmp = {s[i]:1}
            currMax = 1
            currMin = 1
            output += currMax-currMin
            for j in range(i+1, len(s)):
                if s[j] not in hmp:
                    hmp[s[j]] = 0
                hmp[s[j]] +=1
                currMax = max(hmp.values())
                currMin = min(hmp.values())
                output += currMax-currMin
        return output


# previous approach
# class Solution:
#     def beautySum(self, s: str) -> int:
#         def calc(s):
#             hmp = defaultdict(int)
#             for c in s :
#                 hmp[c]+=1
#             return max(hmp.values()) - min(hmp.values())
#         pool = []
#         output = 0
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 pool.append(s[i:j])
#         for p in pool:
#             output += calc(p)
#         return output
#
