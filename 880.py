class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        currSize = 0  # compute the total size of the current string
        for c in S:
            if 48 <= ord(c) <= 57:
                currSize *= int(c)
            else:
                currSize += 1

        for c in S[::-1]:
            K %= currSize
            if K == 0 and 97 <= ord(c) <= 122:  # if current string(from start to curr) is repeating
                return c
            else:  # look further
                if 48 <= ord(c) <= 57:
                    currSize /= int(c)
                else:
                    currSize -= 1


# previous approach
# def decodeAtIndex( S: str, K: int):
#     temp = ""
#     length = 0
#     for i in range(len(S)):
#         if S[i].isdigit() == False:
#             length+=1
#             temp += S[i]
#         else:
#             length = length * int(S[i])
#
#
#
#     for c in reversed(S):
#         K %= length
#         if K == 0 and c.isalpha():
#             return c
#
#         if c.isdigit():
#             length /= int(c)
#         else:
#             length -= 1
#
#
#
#
#
# print( decodeAtIndex(S = "leet2code3", K = 10))
# print(decodeAtIndex("yyuele72abcd2cndsa5", 100))
# # print( decodeAtIndex(S = "ha22", K = 5))
# # print( decodeAtIndex(S = "a2345678999999999999999", K = 1))
# # print( decodeAtIndex(S = "czjkk9elaqwiz7s6kgvl4gjixan3ky7jfdg3kyop3husw3fm289thisef8blt7a7zr5v5lhxqpntenvxnmlq7l34ay3jaayikjps",
# #                      K = 768077956)) #c
# # print( decodeAtIndex(S = "yyuele72uthzyoeut7oyku2yqmghy5luy9qguc28ukav7an6a2bvizhph35t86qicv4gyeo6av7gerovv5lnw47954bsv2xruaej",
# #                      K = 123365626)) #l
#
#
#
