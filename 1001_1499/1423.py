class Solution:
    def maxScore(self, cardPoints: 'List[int]', k: int) -> int:
        s = sum(cardPoints)
        window = len(cardPoints) - k
        curr = sum(cardPoints[:window])
        output = s - curr
        l = 0
        r = window
        while r < len(cardPoints):
            curr -= cardPoints[l]
            curr += cardPoints[r]
            output = max(s-curr,output)
            r+=1
            l+=1
        return output
