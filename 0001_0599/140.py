class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> 'List[str]':
        words = set(wordDict)
        dp = {}

        def helper(rem, words, dp):
            if rem == "": return [[]]
            if rem in dp: return dp[rem]

            for i in range(1, len(rem) + 1):
                curr = rem[:i]
                if curr in words:
                    for following in helper(rem[i:], words, dp):
                        if rem not in dp:
                            dp[rem] = []
                        dp[rem].append([curr] + following)

            if rem not in dp:
                dp[rem] = []
            return dp[rem]

        helper(s, words, dp)

        if s in dp:
            return [" ".join(words) for words in dp[s]]
        else:
            return []
