class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1, s2, s3 = list(s1), list(s2),list(s3)
        def dfs(s1, s2, s3, i, j, check): #i is the pos in s1 , j in the pos in s2
            if (i,j) in check:
                return check[(i,j)]
            elif len(s1) + len(s2) != len(s3):
                check[(i,j)] = False
                return False
            else:
                while s3: #keep taking out from s3, and check if the remaining first letter is from s1 or s2. if s1[0]==s2[0], check each one
                    if s1 and s2 and s1[0]==s2[0]==s3[0]:
                        return dfs(s1[1:].copy(),s2.copy(), s3[1:].copy(), i+1, j, check) | dfs(s1.copy(),s2[1:].copy(), s3[1:].copy(),i, j+1, check) #either take from first one or the second
                    elif s1 and s1[0] == s3[0]:
                        s1.pop(0)
                        s3.pop(0)
                    elif s2 and s2[0] == s3[0]:
                        s2.pop(0)
                        s3.pop(0)
                    else: #it's not from s1, nor s2
                        check[(i,j)] = False
                        return False
                check[(i,j)] = True
                return True
        check = {}
        return dfs(s1,s2,s3,0,0,check)



