class Solution:
    def maxScore(self, s: str) -> int:
        output = -float('inf')
        one = zero = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero+=1
            else:
                one +=1
            output = max(zero-one, output)
        return output + one + (1 if s[-1] == "1" else 0)