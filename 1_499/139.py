class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        def helper(curr, ref, dp):
            if curr in dp:
                return dp[curr]
            elif curr in wordDict:
                dp[curr] = True
                return True
            else:
                temp = ""
                find = []
                for i in range(len(curr)):
                    temp+=curr[i]
                    if temp in wordDict:
                        find.append(curr[i+1:]) #add the rest of curr, this is the list to be checked, recursively
                if find==[]: #any prefix of S cannot be found in dict
                    dp[curr] = False
                    return False
                else:
                    for f in find:
                        if helper(f, wordDict, dp) == True: #check the rest of the string.
                            dp[f] = True
                            return True
                dp[curr] = False
                return False

        return helper(s, wordDict, {})
