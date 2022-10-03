class Solution:
    def equalFrequency(self, word: str) -> bool: # O( N ** 2 | N )
        def valid(w):
            lkp = [0] * 26
            for c in w:
                lkp[ord(c)-ord('a')] += 1 
            return len(set(_ for _ in lkp if _)) == 1 
        
        for i in range(len(word)): #simulation to take each letter, and see if it's valid
            if valid(word[:i] + word[i+1:]):
                return True
        return False
    
    
