class Solution:
    def makeGood(self, s: str) -> str: # O( N | N )
        arr = list(s)
        stk = [arr.pop(0)]
        while arr: # 
            while arr and stk and abs(ord(arr[0]) - ord(stk[-1])) == 32: #check if current character is the lower/upper cased of prev
                stk.pop()
                arr.pop(0)
            if arr:
                stk.append(arr.pop(0))
        
        return "".join(stk)
    



# previous solution

# class Solution:
#     def makeGood(self, s: str) -> str:
#         def isGood(s):
#             if len(s) <= 1:
#                 return [1]
#             else:
#                 for i in range(1, len(s)):
#                     if s[i].lower() == s[i - 1].lower() and s[i] != s[i - 1]:
#                         return [0, i]
#                 return [1]

#         res = isGood(s)
#         while res[0] == 0:
#             s = s[:res[1] - 1] + s[res[1] + 1:]
#             res = isGood(s)
#         return s



