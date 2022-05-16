class Solution:
    def removeAnagrams(self, words: 'List[str]') -> 'List[str]': #O(N | N)
        def stat(w): #count how many times one letter appears in the word
            arr = [0] *26 
            for c in w:
                arr[ord(c)-ord('a')] += 1 
            return arr
        
        prev = stat(words[0])
        output = [words[0]]
        for w in words[1:]: #stacking approach, add if curr != prev
            curr = stat(w)
            if curr != prev:
                output.append(w)
                prev = curr
        return output
    

