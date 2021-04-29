class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        def helper(output, arr, s, e, n):
            while s <= e:
                mid = (s+e)//2
                if arr[mid] < n:
                    s = mid +1
                elif arr[mid] > n:
                    e = mid -1
                elif arr[mid] == n:
                    output[0] = min(output[0], mid)
                    output[1] = max(output[1], mid)
                    helper(output, arr, s, mid-1, n)
                    helper(output, arr, mid+1, e, n)
                    break

        output = [float('inf'), -float('inf')]
        helper(output, nums, 0, len(nums)-1, target)
        if output[0] == float('inf'):
            return [-1,-1]
        else:
            return output


# previous approach
# class Solution:
#     def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
#         l = float('inf')
#         r = -float('inf')
#         s = 0
#         e = len(nums) - 1
#         while s <= e:
#             mid = (s + e) // 2
#             if nums[mid] == target:  # found, and keep searching on the left
#                 l = min(l, mid)
#                 r = max(r, mid)
#                 s = mid + 1
#             elif nums[mid] < target:
#                 s = mid + 1
#             elif nums[mid] > target:
#                 e = mid - 1
#         s = 0
#         e = len(nums) - 1
#         while s <= e:
#             mid = (s + e) // 2
#             if nums[mid] == target:  # found, and keep searching on the right
#                 l = min(l, mid)
#                 r = max(r, mid)
#                 e = mid - 1
#             elif nums[mid] < target:
#                 s = mid + 1
#             elif nums[mid] > target:
#                 e = mid - 1
#
#         return [l, r] if l != float('inf') else [-1, -1]


