class Solution:
    def countConsistentStrings(self, allowed: str, words: 'List[str]') -> int:
        return len([ w for w in words if  set(list(w)) - set(list(allowed)) == set() ] )