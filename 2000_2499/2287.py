class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int: #O(N | 1)
        a = [0] * 26 # record the occurrence of each character
        b = [0] * 26 # record the occurrence of each character
        for c in s: 
            a[ord(c)-ord('a')] += 1
        for c in target:
            b[ord(c)-ord('a')] += 1 
        
        output = float('inf')
        for i in range(len(b)):
            if b[i] != 0:
                if a[i] == 0:
                    return 0
                else:
                    output = min(output, a[i]//b[i]) # to check how many times a can form b on this character
        return output
    
    
