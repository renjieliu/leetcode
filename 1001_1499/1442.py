class Solution:
    def countTriplets(self, arr: 'List[int]') -> int:
        dp = [[None for _ in range(len(arr))] for _ in range(len(arr))]
        stk = []
        output = 0
        for r in range(len(arr)):
            curr = arr[r]
            stk.append({})  # using hmp to record how many times curr val occur
            dp[r][r] = curr
            if curr not in stk[-1]:
                stk[-1][curr] = 0
            stk[-1][curr] += 1
            for c in range(r + 1, len(arr)):
                curr ^= arr[c]
                dp[r][c] = curr
                if curr not in stk[-1]:
                    stk[-1][curr] = 0
                stk[-1][curr] += 1
        for r in range(len(arr)):
            for c in range(r + 1, len(arr)):
                curr = dp[r][c - 1]
                if curr in stk[c]:
                    output += stk[c][curr]
        return output
