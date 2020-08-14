class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        odd = [v for v in hmp.values() if v % 2 != 0]
        even = [v for v in hmp.values() if v % 2 == 0]
        maxOdd = max(odd) if odd else 0
        contribute = [o - 1 for o in odd]  # take max(evenNumber) from the odd , 1--> 0, 3 --> 2,
        return sum(even) + sum(contribute) + maxOdd - ((maxOdd - 1) if maxOdd else 0)  # maxOdd has been added twice

# previous approach
# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     len = 0
#     max_odd = 0
#     map = {}
#     key = ""
#     for i in s:
#         if i in map:
#             map[i]+=1
#         else:
#             map[i] = 1
#
#     for k, v in map.items():
#         if v%2==0:
#             len+=v
#         else:
#             if v > max_odd:
#                 max_odd = v
#                 key = k
#
#     for k, v in map.items():
#         if v%2 != 0:
#             if key == k:
#                 len += v
#             else:
#                 len +=v-1
#     return len
#
# print(longestPalindrome("abccccdd"))
# print(longestPalindrome("absdfasfasdfcccd"))
# print(longestPalindrome("absdfaasssdfasdfsafasfsdfsafdsfasdfcccd"))
#
#
