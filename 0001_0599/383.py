class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  # O( N | N )
        def counter(w): #count the occurrence of each character in w
            output =  {}
            for c in w:
                if c not in output:
                    output[c] = 0
                output[c] += 1 
            return output 
    
        lkp_r = counter(ransomNote)
        lkp_m = counter(magazine)
        
        for k, v in lkp_r.items(): # check if all the characters in ransomNote are in magazine, with enough occurrence
            if k not in lkp_m or lkp_m[k] < v:
                return False
        return True


    

# previous solution

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         hmp = {}
#         for m in magazine:
#             if m not in hmp:
#                 hmp[m] = 0
#             hmp[m] +=1
#         for r in ransomNote:
#             if r not in hmp:
#                 return False
#             else:
#                 hmp[r] -=1
#                 if hmp[r] == 0:
#                     del hmp[r]
#         return True


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