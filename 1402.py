class Solution:
    def maxSatisfaction(self, satisfaction: 'List[int]') -> int:
        s = sorted(satisfaction)
        if s[-1] <= 0:
            return 0
        elif s[0] >= 0:
            return sum([(i + 1) * c for i, c in enumerate(s)])
        else:
            arr = []
            arr_neg = []
            for c in s:
                if c < 0:
                    arr_neg.append(c)
                else:
                    arr.append(c)
            curr = sum([(i + 1) * c for i, c in enumerate(arr)])
            for a in arr_neg[::-1]:  # the close to 0, the less side effect
                arr = [a] + arr
                curr = max(curr, sum([(i + 1) * c for i, c in enumerate(arr)]))
            return curr

