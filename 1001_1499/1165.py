class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int: # O( N | 26 )
        loc = {k: i for i, k in enumerate(keyboard)} # record the location of each letter
        output = loc[word[0]] # initialize the output
        for i in range(1, len(word)):
            output += abs( loc[word[i]] - loc[word[i-1]] ) # calc the moving distance
        return output
    



# previous solution

# class Solution:
#     def calculateTime(self, keyboard: str, word: str) -> int:
#         dp = []
#         hmp = {c:i for i, c in enumerate(keyboard) }
#         word = keyboard[0] + word #put first keyboard letter in front of the word, to calculate the first move
#         for i in range(1,len(word)):
#             dp.append(abs(hmp[word[i]] - hmp[word[i-1]]) )
#         return sum(dp)


# previous approach
# class Solution:
#     def calculateTime(self, keyboard: str, word: str) -> int:
#         hmp = {}
#         for i in range(len(keyboard)):
#             hmp[keyboard[i]] = i
#         prev = 0
#         output = 0
#         for c in word:
#             output += abs(hmp[c]-prev)
#             prev = hmp[c]
#         return output