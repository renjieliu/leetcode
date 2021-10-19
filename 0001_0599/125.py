class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        for c in s.lower():
            if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90 or 48 <= ord(c) <= 57:
                forward += c

        backward = ""
        for c in s.lower()[::-1]:
            if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90 or 48 <= ord(c) <= 57:
                backward += c

        return backward == forward

# previous approach
# def isPalindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     dict = "abcdefghijklmnopqrstuvwxyz01234565789"
#     output = ""
#     output_r = ""
#     for i in str(s).lower():
#         if i in list(dict):
#             output += i
#             output_r = i+output_r
#
#     if output_r ==output:
#         return True
#     else:
#         return False
#
# print(isPalindrome(""))

