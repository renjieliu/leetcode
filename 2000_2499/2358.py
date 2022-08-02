class Solution:
    def maximumGroups(self, grades: 'List[int]') -> int: #O( 1 | 1 )
        return int(-1 + (1+8*len(grades))**0.5)//2       # (1+n)*n//2 <= len(grades), return n
    
    
