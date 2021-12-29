class Solution:
    def groupStrings(self, strings: 'List[str]') -> 'List[List[str]]':
        lkp = {}
        for i in range(97, 123): #generate the letter lookup table
            lkp[i] = chr(i)
        for i in range(123, 123+26):
            lkp[i] = chr(i-26)
        
        def transform(s): # transform the first letter to 'z', and the rest to corresponding letter
            # print(s)
            delta = ord('z') - ord(s[0])
            output = ""
            for c in s:
                output += lkp[ord(c) + delta]
            return output
        
        hmp = {} 
        for s in strings: 
            t = transform(s)
            if t not in hmp:
                hmp[t] = []
            hmp[t].append(s)
        return hmp.values()
    
    

    
