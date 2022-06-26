class Solution:
    def maxScore(self, cardPoints: 'List[int]', k: int) -> int: #O( N | 1 )
        output = curr = sum(cardPoints[-k:])
        right = len(cardPoints) #it's like attaching the same array to the end of the current array.
        while right < len(cardPoints)+k: #sliding window from -k of the array, and moving to len(cardPoints)+k-1
            curr -= cardPoints[right-k] # take out the previous one
            curr += cardPoints[right%len(cardPoints)] #the real index in the original array
            output = max(output, curr)
            right += 1
            # print(curr)
        return output
    

# previous solution 

# class Solution:
#     def maxScore(self, cardPoints: 'List[int]', k: int) -> int:
#         s = sum(cardPoints)
#         window = len(cardPoints) - k
#         curr = sum(cardPoints[:window])
#         output = s - curr
#         l = 0
#         r = window
#         while r < len(cardPoints):
#             curr -= cardPoints[l]
#             curr += cardPoints[r]
#             output = max(s-curr,output)
#             r+=1
#             l+=1
#         return output
