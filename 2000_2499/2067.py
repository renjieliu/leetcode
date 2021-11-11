class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        output = 0 
        for n in range(1, 27): #assuming it has n unique letters 
            hmp = {} 
            size = n * count # this is the length of the assuming substring
            letterCnt = 0
            for i, c in enumerate(s):
                if c not in hmp:
                    hmp[c] = 0
                hmp[c] += 1 
                if hmp[c] == count:
                    letterCnt += 1 
                
                if i >= size: #sliding windows to take out the letter on the left side
                    left = s[i-size]
                    if hmp[left] == count:
                        letterCnt-=1
                    hmp[left]-=1 
                    if hmp[left] == 0:
                        del hmp[left]
            
                if letterCnt == n: #all the letters appear count times
                    output += 1 
            
        return output
                    

