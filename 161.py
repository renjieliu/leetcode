class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t))>1: return False
        if len(s) == len(t): #option 1: replace 1 character
            cnt = 0
            for i in range(len(s)):
                cnt += 1 if s[i] != t[i] else 0
            return cnt == 1
        else: #option 2: insert or delete, essentially the same. 'insert to the short' = 'delete from the long'
            longer = list(s if len(s) > len(t) else t)
            shorter = list(s if len(s) < len(t) else t)
            i = 0
            cnt = 0
            while i < len(shorter):
                if shorter[i] != longer[i]:
                    if cnt == 0:
                        shorter.insert(i, longer[i])
                        cnt += 1
                    else:
                        return False
                i+=1
                #print(shorter)
            return True # if everthing is same, then the diff happens at the end



# previous approach
# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         if abs(len(s) - len(t)) > 1:
#             return False
#         elif abs(len(s) - len(t)) == 1:  # if diff is 1, go thru the string, and compare each position.
#             short = s if len(s) < len(t) else t
#             long = t if short == s else s
#             diff = 0
#             while short and long:
#                 if short[0] == long[0]:
#                     short = short[1:]
#                     long = long[1:]
#                 else:
#                     diff += 1
#                     long = long[1:]
#             return True if diff <= 1 else False  # if diff = 0, meaning the short is exausted and the last char mismatches.  if diff==1: satisfy the problem
#
#         elif len(s) == len(t):  # go thru the string, and compare each position.
#             diff = 0
#             while s:
#                 if s[0] != t[0]:
#                     diff += 1
#                 s = s[1:]
#                 t = t[1:]
#             return True if diff == 1 else False
