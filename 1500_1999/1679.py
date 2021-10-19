class Solution:
    def maxOperations(self, nums: 'List[int]', k: int) -> int:
        def bin(arr, n, s, e): #this is to find the right most loc of n
            s = s+1
            output = -1
            while s<=e :
                mid = (s+e)//2
                if arr[mid] == n:
                    output = mid
                    s = mid +1
                elif arr[mid] < n:
                    s = mid +1
                elif arr[mid] > n:
                    e = mid - 1
            return output

        cnt = 0
        nums.sort()
        l = 0
        r = len(nums)-1
        while l <= r:
            loc = bin(nums, k-nums[l], l, r) #to find the k-x in the remaining array
            if loc != -1:
                r = loc-1 # move the right pointer to the right position
                cnt += 1
            l+=1

        return cnt





# previous approach
# class Solution:
#     def maxOperations(self, nums: 'List[int]', k: int) -> int:
#         hmp = {}
#         for n in nums:
#             if n not in hmp:
#                 hmp[n] = 0
#             hmp[n] += 1
#         output = 0
#         for n in nums:
#             if n in hmp:
#                 if k - n in hmp:
#                     if n == k - n:  # if the rem is the same as n , the same number needs to be taken out twice
#                         if hmp[n] >= 2:
#                             hmp[n] -= 2
#                             output += 1
#                             if hmp[n] <= 0:
#                                 del hmp[n]
#                     else:
#                         hmp[n] -= 1
#                         hmp[k - n] -= 1
#                         output += 1
#                         if hmp[n] <= 0:
#                             del hmp[n]
#                         if hmp[k - n] <= 0:
#                             del hmp[k - n]
#
#         return output
#
#
#
#
#
#
#
#
