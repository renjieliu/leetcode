class Solution:
    def countSmaller(self, nums: 'List[int]') -> 'List[int]':
        # implement segment tree
        def update(index, value, tree, size):
            index += size  # shift the index to the leaf
            # update from leaf to root
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        def query(left, right, tree, size):
            # return sum of [left, right)
            result = 0
            left += size  # shift the index to the leaf
            right += size
            while left < right:
                # if left is a right node
                # bring the value and move to parent's right node
                if left % 2 == 1:
                    result += tree[left]
                    left += 1
                # else directly move to parent
                left //= 2
                # if right is a right node
                # bring the value of the left node and move to parent
                if right % 2 == 1:
                    right -= 1
                    result += tree[right]
                # else directly move to parent
                right //= 2
            return result

        offset = 10**4  # offset negative to non-negative
        size = 2 * 10**4 + 1  # total possible values in nums
        tree = [0] * (2 * size)
        result = []
        for num in reversed(nums):
            smaller_count = query(0, num + offset, tree, size)
            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)

#my approach, failed, need to better understand the relationship of original arr, segment tree, seg node, node start and node end

# class Solution:
#     def countSmaller(self, nums: 'List[int]') -> 'List[int]':
#         for i in range(len(nums)):
#             nums[i] += 10000
#         n = max(nums)  # there could be 20001 possiblities of n
#         total = 1
#         layer = 0
#         while 2 ** layer < n:
#             layer += 1
#             total += 2 ** layer
#         seg = [0] * total
#
#         def query(seg, node, seg_start, seg_end, q_start, q_end):
#             if seg_start == seg_end:
#                 return seg[node]
#             elif q_start <= seg_start <= seg_end <= q_end:
#                 return seg[node]
#             elif seg_end < q_start or seg_start > q_end:
#                 return 0
#             else:
#                 mid = (seg_start + seg_end) // 2
#                 left = query(seg, node * 2 + 1, seg_start, mid, q_start, q_end)
#                 right = query(seg, node * 2 + 2, mid + 1, seg_end, q_start, q_end)
#                 return left + right
#
#         def update(seg, node, idx, start, end):  # idx is the value in the original arr
#             if start == end:
#                 seg[node] += 1
#             else:
#                 mid = (start + end) // 2
#                 if idx <= mid:
#                     update(seg, node * 2 + 1, idx, start, mid)
#                 else:
#                     update(seg, node * 2 + 2, idx, mid + 1, end)
#                 seg[node] = seg[node * 2 + 1] + seg[node * 2 + 2]
#
#         output = []
#
#         for i in range(len(nums) - 1, -1, -1):
#             curr = nums[i]
#             output.append(query(seg, 0, 0, n - 1, 0, curr - 1))  # sum smaller number in the segTree
#             update(seg, 0, curr, 0, n - 1)
#         return output[::-1]
#
#
#
#
#
#
#
#
#
#
#
#
#
