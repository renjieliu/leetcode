class Solution:
    def checkDistances(self, s: str, distance: 'List[int]') -> bool: # O( N | 26 )
        lkp = [[] for _ in range(26)] 
        for i, c in enumerate(s): # record the location of each character
            lkp[ord(c) - ord('a')].append(i)
        
        for i, d in enumerate(distance): # compare the location diff with the distance
            if lkp[i] and lkp[i][1] - lkp[i][0] - 1 != d: # gap = b-a-1
                return False
        return True

    
