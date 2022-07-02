class Solution:
    def maxBoxesInWarehouse(self, boxes: 'List[int]', warehouse: 'List[int]') -> int: # O(NlogN | N)
        dp = [warehouse[0]] 
        for w in warehouse[1:]: #make the dp monotone stack
            dp.append(min(dp[-1], w))
        
        dp = dp[::-1]
        boxes.sort()
        cnt = 0
        while boxes and dp:
            while boxes and dp and boxes[0] > dp[0]: # accomodate the next smallest box.
                dp.pop(0) #these slots cannot be used
            
            if boxes and dp and boxes[0] <= dp[0]:
                cnt += 1 
                boxes.pop(0)
                dp.pop(0)
        return cnt
        
        

        
# previous solution

# class Solution:
#     def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
#         minStk = [warehouse[0]]  # minHeight on the left
#         for i in range(1, len(warehouse)):
#             minStk.append(min(minStk[-1], warehouse[i]))
#         cnt = 0
#         boxes.sort()
#         for m in minStk[::-1]:  # to check if there's boxes can be pushed from the left
#             if boxes[0] <= m:
#                 cnt += 1
#                 boxes.pop(0)
#                 if len(boxes) == 0:
#                     return cnt
#         return cnt

