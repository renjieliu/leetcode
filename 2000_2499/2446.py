class Solution:
    def haveConflict(self, event1: 'List[str]', event2: 'List[str]') -> bool: # O( 1 | 1 )
        return not(event2[0] > event1[1] or event1[0] > event2[1]) # reverse of non intersection
    
    
