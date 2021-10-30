class Solution:
    def kthDistinct(self, arr: 'List[str]', k: int) -> str:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0 
            hmp[a] += 1 
        seq = 0
        for a in arr:
            if hmp[a] == 1:
                if seq+1 == k:
                    return a
                else:
                    seq+=1
        
        return ""
    
    
