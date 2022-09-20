class Solution:
    def findLength(self, nums1: 'List[int]', nums2: 'List[int]') -> int: # O( MN | MN )
        dp = [[0 for _ in range(len(nums1)+1)] ]  # pad the first line as 0 to avoid row-1 complex
        output = 0
        for r in range(1, len(nums1) + 1):
            dp.append([0])
            for c in range(1, len(nums2)+1):
                if nums1[r-1] == nums2[c-1]: #if same, add 1 to dp[r-1][c-1]
                    dp[-1].append(dp[r-1][c-1] + 1)
                    output = max(output, dp[-1][-1])
                else:
                    dp[-1].append(0) # cut off the continuous match
                # print(dp)
        return output



# previous solution

# class Solution:
#     def findLength(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
#         def valid(arr1, arr2, v):
#             combo = set()
#             for i in range(len(nums2)+1-v):
#                 combo.add(tuple(nums2[i:i+v]))

#             for i in range(len(nums1)):
#                 if tuple(nums1[i:i+v]) in combo:
#                     return True
#             return False


#         s = 0
#         e = len(nums1)
#         ans = 0
#         while s <= e: # binary search to find the arr length which is valid for both lists
#             mid = (s+e)//2
#             if valid(nums1, nums2, mid):
#                 ans = max(ans, mid)
#                 s = mid +1
#             else:
#                 e = mid -1

#         return ans




