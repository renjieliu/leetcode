class Solution:
    def appendCharacters(self, s: str, t: str) -> int: # O( N | 1 )
        i = j = 0
        while i < len(s):
            if s[i] == t[j]: # if current letter in s is same as current first letter in t
                j += 1 
                if j == len(t):
                    return 0
            i += 1 
        
        return len(t) - j #how many letters left from t

