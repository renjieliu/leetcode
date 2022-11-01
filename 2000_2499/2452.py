class Solution:
    def twoEditWords(self, queries: 'List[str]', dictionary: 'List[str]') -> 'List[str]': # O( K*N**2 | N ), k being the word length
        output = [] 
        n = len(queries[0]) # all the words are with the same length
        for q in queries: # check each words, and see if the diff is <= 2
            for d in dictionary: 
                if len([1 for i in range(n) if q[i] != d[i]]) <= 2:
                    output.append(q)
                    break 
        return output

        
