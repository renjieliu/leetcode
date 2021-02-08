class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmp = {}
        for m in magazine:
            if m not in hmp:
                hmp[m] = 0
            hmp[m] +=1
        for r in ransomNote:
            if r not in hmp:
                return False
            else:
                hmp[r] -=1
                if hmp[r] == 0:
                    del hmp[r]
        return True


# def canConstruct(ransomNote, magazine):
#     """
#     :type ransomNote: str
#     :type magazine: str
#     :rtype: bool
#     """
#     t = magazine
#     if ransomNote =="":
#         return True
#     else:
#         for x in ransomNote:
#             if x in t:
#                 t=t.replace(x, "", 1)
#             else:
#                 return False
#
#         return True


# print(canConstruct("aa", "ab"))
# print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))