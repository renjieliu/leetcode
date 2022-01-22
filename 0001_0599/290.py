class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def match(A, B):
            if len(A) != len(B):
                return False 
            hmp_A = {}  
            hmp_B = {}
            for i, a in enumerate(A):
                b = B[i]
                if a not in hmp_A: # compare from A to B
                    hmp_A[a] = B[i]
                elif hmp_A[a] != B[i] :
                    return False
                
                if b not in hmp_B: # compare from B to A
                    hmp_B[b] = a
                elif hmp_B[b] != a :
                    return False
            return True
        
        A = list(pattern) 
        B = s.split(' ')
        return match(A, B) 
        


# previous approach

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         def match(A, B):
#             if len(A) != len(B):
#                 return False 
#             hmp = {}
#             for i, a in enumerate(A):
#                 if a not in hmp:
#                     hmp[a] = B[i]
#                 elif hmp[a] != B[i] :
#                     return False
#             return True
#         A = list(pattern) 
#         B = s.split(' ')
#         return match(A, B) and match(B, A) #need to match A to B, and B to A
        



# previous approach

# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
#         pattern = list(pattern)
#         arr = str.split(' ')
#         if len(pattern) != len(arr):
#             return False
#         else:
#             hmp_p = {}
#             hmp_a = {}
#             for i, p in enumerate(pattern):
#                 # print(hmp_p, hmp_a)
#                 if p not in hmp_p:
#                     if arr[i] not in hmp_a:
#                         hmp_p[p] = arr[i]
#                         hmp_a[arr[i]] = p
#                     else:
#                         if hmp_a[arr[i]] != p:
#                             return False
#                         else:
#                             continue
#                 else:
#                     if hmp_p[p] != arr[i]:
#                         return False
#                     else:
#                         continue
#             return True

