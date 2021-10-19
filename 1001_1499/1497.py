class Solution:
    def canArrange(self, arr: 'List[int]', k: int) -> bool:
        hmp = {}
        for a in arr: # for modular number, to check if we can find k-mod in the array
            if a%k not in hmp:
                hmp[a%k] = 0
            hmp[a%k] += 1
        for key, v in hmp.items():
            if key==0:
                if v%2!=0: return False
            elif k-key not in hmp or v!=hmp[k-key] :
                return False
        return True