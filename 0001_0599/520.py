class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_cnt = 0
        for i, c in enumerate(word): #just go through and check if the letter is in upper case
            upper_cnt +=1 if 65 <= ord(c) <= 90 else 0
        return upper_cnt==0 or upper_cnt == len(word) or (upper_cnt==1 and 65 <= ord(word[0]) <= 90) 
        #return word == word.upper() or word == word[0].upper()+word[1:].lower() or word == word.lower()
    


# previous approach

# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         upperLoc = []
#         for i, c in enumerate(word):
#             if 65<= ord(c) <= 90:
#                 upperLoc.append(i)
#         if len(upperLoc) == len(word) or len(upperLoc) == 0 or (len(upperLoc) == 1 and upperLoc[0] == 0):
#             return True
#         return False



# previous approach
# def detectCapitalUse(word):
#     """
#     :type word: str
#     :rtype: bool
#     """
#     output = False
#     lower = 0
#     upper = 0
#     for i in range(0, len(word)):
#         if ord(word[i]) >= 97:
#             lower += 1
#         else:
#             upper += 1
#     if (lower ==len(word) or upper == len(word)) or ((ord(word[0])<97 and lower == len(word) -1)):
#         output = True
#
#     return output
#
#
# print(detectCapitalUse("Google"))
# print(detectCapitalUse("GOOGLE"))
# print(detectCapitalUse("g"))
# print(detectCapitalUse("apple"))
# print(detectCapitalUse("apPle"))
#




