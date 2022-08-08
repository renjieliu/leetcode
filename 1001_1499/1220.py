class Solution:
    def countVowelPermutation(self, n: int) -> int: #O( N | N )
        def helper(hmp, rem, curr, rules): # how many permutations from current, with current character and rem length 
            if (curr, rem) in hmp:
                return hmp[(curr, rem)]
            elif rem == 1:
                hmp[(curr, rem)] = 1                
            else:
                hmp[(curr, rem)] = 0
                for c in rules[curr]:
                    hmp[(curr, rem)] += helper(hmp, rem-1, c, rules)
            return hmp[(curr, rem)]
        
        rules = {"a": ["e"], "e":["a", "i"], "i": ["a", "e", "o", "u"],  "o": ["i", "u"], "u": ["a"]} # this is the rules from the question
        hmp = {}
        for c in "aeiou": # start with a, e, i, o, u
            helper(hmp, n, c, rules)
        output = hmp[("a", n)] + hmp[("e", n)]+ hmp[("i", n)]+ hmp[("o", n)]+ hmp[("u", n)]
        return output % (10**9+7)
    
    
    

# previous solution 

# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         mod = 10 ** 9 + 7
#         follow = {'a': ['e'], 'e': ["a", "i"], 'i': ["a", "e", "o", "u"], "o": ["i", "u"], "u": ["a"]}
#         dp = {'a': {}, 'e': {}, 'i': {}, "o": {}, "u": {}}

#         def helper(follow, dp, curr, rem):
#             if rem in dp[curr]:
#                 return dp[curr][rem]
#             else:
#                 dp[curr][rem] = 0
#                 if rem == 0:
#                     dp[curr][rem] = 1
#                 else:
#                     for f in follow[curr]:
#                         dp[curr][rem] += helper(follow, dp, f, rem - 1)
#                 return dp[curr][rem]

#         output = 0
#         for c in 'aeiou':
#             helper(follow, dp, c, n - 1)  # since we have used c as the start, we have n-1 remaining
#             output += dp[c][n - 1]  # use current as start, how many can form with n-1 left
#         # print(dp)
#         return output % mod



