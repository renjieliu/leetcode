class Solution:
    def widestPairOfIndices(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        diff = {}
        output = s1 = s2 = 0
        for loc, (a, b) in enumerate(zip(nums1, nums2)):
            s1 += a  # prefix of nums1
            s2 += b  # prefix of nums2
            if s2 - s1 not in diff:  # total of nums2 - total of nums1
                diff[s2 - s1] = loc
            if s2 == s1:  # total sum is same up till now
                output = loc + 1
            else:
                output = max(output, loc - diff[s2 - s1])  # if s2-s1 is met before, current gap is equal.
        return output


# previous approach
# class Solution:
#     def widestPairOfIndices(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
#         diff = {0: -1}
#         output = s1 = s2 = 0
#         for loc, (a, b) in enumerate(zip(nums1, nums2)):
#             s1 += a  # prefix of nums1
#             s2 += b  # prefix of nums2
#             if s2 - s1 not in diff:  # total of nums2 - total of nums1
#                 diff[s2 - s1] = loc
#             else:
#                 output = max(output, loc - diff[s2 - s1])  # if s2-s1 is met before, current gap is equal.
#         return output
#
