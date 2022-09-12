class Solution:
    def bagOfTokensScore(self, tokens: 'List[int]', power: int) -> int: # O( NlogN | 1 )
        tokens.sort()
        score = 0 
        output = 0
        while tokens:
            if power >= tokens[0]:
                power -= tokens.pop(0) #take out the smallest power
                score +=1
                output = max(score, output)
            elif score > 0: # add the largest power
                power += tokens.pop()
                score -= 1
                output = max(score, output)
            else: #not enough power or score to play the next round
                return output          
        return output
    



# previous solution

# class Solution(object):
#     def bagOfTokensScore(self, tokens, P):
#         tokens.sort()
#         output = curr = 0
#         while tokens and (P >= tokens[0] or curr!=0):
#             while tokens and P >= tokens[0]:
#                 P -= tokens.pop(0)
#                 curr += 1
#             output = max(output, curr)

#             if tokens and curr:
#                 P += tokens.pop()
#                 curr -= 1

#         return output



