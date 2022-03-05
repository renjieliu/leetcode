class Solution:
    def numberOfArithmeticSlices(self, nums: 'List[int]') -> int:
        gauss = lambda x: ( (1 + (x-3+1) ) * (x-3+1)//2 ) if x >= 3 else 0   # A = 1 , B = x-3+1, sum from A to B
        if len(nums) < 3: return 0
        output = 0
        prev = nums[1] - nums[0]
        cnt = 2
        for r in range(2, len(nums)):
            diff = nums[r] - nums[r-1]
            if diff != prev:
                output += gauss(cnt) #if the length of the subarray is 4, it has 1 length(4) + 2 length (3) subarray              
                prev = diff
                cnt = 2
            else:
                cnt += 1
        output += gauss(cnt)       
        
        return output
                
            

# class Solution:
#     def numberOfArithmeticSlices(self, A: 'List[int]') -> int:
#         if len(A) < 3: return 0
#         l = 0
#         r = 1
#         cnt = 0
#         currDiff = A[r] - A[l]
#         while r < len(A):
#             if A[r] - A[r-1] != currDiff:
#                 length = r-1 -l+1
#                 cnt += 0 if length < 3 else (1+length-2) * (length-2)//2 #3-->1, 4-->2...sum = (1+n)*n//2
#                 currDiff = A[r] - A[r-1]
#                 l = r-1
#             r+=1
#         length = r-1 -l+1
#         cnt += 0 if length < 3 else (1+length-2) * (length-2)//2 #3-->1, 4-->2...sum = (1+n)*n//2

#         return cnt






