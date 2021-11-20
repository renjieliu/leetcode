class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        def counter(word):
            hmp = defaultdict(lambda:0)
            for w in word:
                hmp[w] += 1
            return hmp
    
        hmp1 = counter(word1)
        hmp2 = counter(word2)
        for k, v in hmp1.items(): #from word1 to word2, to avoid cases like word1 = "zzzyyy", word2 = "iiiiii"
            if v - hmp2[k] > 3:
                return False 
            
        for k, v in hmp2.items(): #from word2 to word1, to avoid cases like word1 = "zzzyyy", word2 = "iiiiii"
            if v - hmp1[k] > 3:
                return False        
        
        return True
        
 