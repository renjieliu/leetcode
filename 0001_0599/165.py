class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(_) for _ in version1.split('.')]
        v2 = [int(_) for _ in version2.split('.')]
        i = 0 
        while i < len(v1) and i < len(v2):
            if v1[i] > v2[i]: #if v1 version is smaller
                return 1
            elif v1[i] < v2[i]: #if v1 version is larger
                return -1
            i+=1
        t = sum(v1[i:]) - sum(v2[i:])
        return -1 if t <= -1 else (1 if t >= 1 else 0 ) # for example, if v2 got something left, sum(v2[i:]) will be > sum(v1[i:])

    
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1 = version1.split('.')
#         v2 = version2.split('.')
#         if len(v1) < len(v2): #padd both version to be the same length
#             v1 += ['0'] * (len(v2) - len(v1))
#         else:
#             v2 += ['0'] * (len(v1) - len(v2))
        
#         while v1 and v2:
#             if int(v1[0]) > int(v2[0]): #if v1 version is smaller
#                 return 1
#             elif int(v1[0]) < int(v2[0]): #if v1 version is larger
#                 return -1
#             v1.pop(0)
#             v2.pop(0)
#         return 0 # they are the same version
    



# previous approach

# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1 = version1.split('.')
#         v2 = version2.split('.')
#         if v1 < v2:
#             v1+=[0] * (len(v2) - len(v1))
#         else:
#             v2+=[0] * (len(v1) - len(v2))
#         while v1 and v2:
#             x = int(v1.pop(0))
#             y = int(v2.pop(0))
#             if x < y :
#                 return -1
#             elif x > y :
#                 return 1
#         return 0


