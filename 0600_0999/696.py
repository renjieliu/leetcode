class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr = [0,0]
        cnt = 0
        if s[0] == "0":
            arr[0]+=1
        else:
            arr[1]+=1
        for i in range(1, len(s)): # check continuous 0 and 1
            if s[i] == s[i-1]:
                arr[int(s[i])] += 1
            else:
                if arr[0] * arr[1] != 0:
                    cnt += min(arr[0], arr[1]) #count the min(cnt(0), cnt(1)), reset the counter
                    arr[int(s[i])] = 1
                else:
                    arr[int(s[i])] += 1

        cnt += min(arr[0], arr[1])
        return cnt




# previous approach
# def countBinarySubstrings(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#
#     cnt_1 = 1
#     cnt_2 = 0
#     output = 0
#     ref = s[0]
#
#     for i in range(1, len(s)):
#         if s[i]==ref and s[i] == s[i-1]:
#             cnt_1 += 1
#
#         elif s[i]!=ref:
#             cnt_2 += 1
#
#         elif s[i]==ref and s[i] != s[i-1]:
#             output += (cnt_1 if cnt_1 <= cnt_2 else cnt_2)
#             ref = s[i-1]
#             cnt_1=cnt_2
#             cnt_2 = 1
#
#     output += (cnt_1 if cnt_1 <= cnt_2 else cnt_2)
#
#     return output
# #
# print(countBinarySubstrings("00110011")) #6
# print(countBinarySubstrings("10101")) #4
# print(countBinarySubstrings("00110")) #3
# print(countBinarySubstrings("00100010101010101010101010100110")) #27
# print(countBinarySubstrings("00100010101010101010101010100110001000101010101010101010101001100010001010101010101010100000000000000000000011111111111111111101001100010001010101010101010101010011000100010101010101010101010100110")) #156
# print(countBinarySubstrings("10")) #1



