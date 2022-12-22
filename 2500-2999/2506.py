class Solution:
    def similarPairs(self, words: 'List[str]') -> int: # O( N | N )
        def helper(w): # turn the word to tuple
            arr = [0] * 26 
            for c in w:
                arr[ord(c) - ord('a')] = 1 #just to flag is the letter is seen
            return tuple(arr)
    
        fact = lambda x: 1 if x in (0, 1) else fact(x-1)*x
        combo = lambda x, y: fact(x) //(fact(x-y) * fact(y))
        cnt = defaultdict(lambda: 0)
        
        for w in words: # get the tuple form of each word
            cnt[helper(w)] += 1 
        
        output = 0
        for k, v in cnt.items(): # combination(n, 2) to calc the pairs
            output += combo(v, 2) if v >= 2 else 0
        
        return output


        


# previous solution

# class Solution:
#     def similarPairs(self, words: 'List[str]') -> int: # O( N**2 | 1 )
#         cnt = 0 
#         for i in range(len(words)): # to check if set(each word) is same
#             for j in range(i+1, len(words)):
#                 cnt += set(words[i]) == set(words[j])
#         return cnt

    
