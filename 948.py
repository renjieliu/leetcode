class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        output = curr = 0
        while tokens and (P >= tokens[0] or curr!=0):
            while tokens and P >= tokens[0]:
                P -= tokens.pop(0)
                curr += 1
            output = max(output, curr)

            if tokens and curr:
                P += tokens.pop()
                curr -= 1

        return output