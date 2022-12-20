class Solution:
    def similarPairs(self, words: 'List[str]') -> int: # O( N**2 | 1 )
        cnt = 0 
        for i in range(len(words)): # to check if set(each word) is same
            for j in range(i+1, len(words)):
                cnt += set(words[i]) == set(words[j])
        return cnt

    
