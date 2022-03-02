class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = ptr_t = 0 # pointer on s, and pointer on t
        
        while ptr_s < len(s) and ptr_t < len(t): #check if current character of s can find a match in the rest of t
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t+=1 
        return ptr_s == len(s) #see if the pointer on s is moved to the end of the s 

    



# previous approach

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True 
#         for i in range(len(t)): #find the first character in t, same as s[0], then check the rest
#             if t[i] == s[0]:
#                 return self.isSubsequence(s[1:], t[i+1:])
#         return False


#previous approach

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         ptr = 0
#         for c in s:
#             if c in t[ptr:]:
#                 ptr += t[ptr:].index(c)+1
#             else:
#                 return False
#         return True



# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         temp = ""
#         for i in t:
#             if i in s:
#                 temp +=i

#         for i in s:
#             x = temp.find(i)
#             if x!=-1:
#                 temp = temp[x+1:]
#             else:
#                 return False

#         return True

