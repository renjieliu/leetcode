class Solution:
    def maxScore(self, cardPoints: 'List[int]', k: int) -> int:
        output = curr = sum(cardPoints[:k]) # assume all the numbers from left
        for i in range(k): # move the array to the left, and add the elements from the end
            curr = curr - cardPoints[k-i-1]  + cardPoints[-(i+1)]
            output = max(output, curr)
        return output