class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        i = 0
        while i < len(word1) and i < len(word2):
            output+=word1[i] + word2[i]
            i+=1
        if i < len(word1):
            output+= word1[i:]
        elif i < len(word2):
            output+=word2[i:]
        return output


# previous apparoach
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         output = ""
#         a = list(word1)
#         b = list(word2)
#         while a and b:
#             output+=a.pop(0)
#             output+=b.pop(0)
#         return output+ ("".join(a) if len(a) > 0 else "".join(b))


