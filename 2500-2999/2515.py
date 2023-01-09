class Solution:
    def closetTarget(self, words: 'List[str]', target: str, startIndex: int) -> int: # O( N | 1 )
        if target not in words:
            return -1 
        A = 0 
        i = startIndex 
        while words[i % len(words)] != target: # move forward
            A += 1
            i += 1
        
        B = 0 
        j = startIndex
        while words[j] != target: # move backward
            B += 1
            j -= 1 
        return min(A, B)
    

