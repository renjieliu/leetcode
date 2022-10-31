class Solution:
    def oddString(self, words: 'List[str]') -> str: # O( Nk | Nk), k being the length of the longest word in the words
        hmp = defaultdict(lambda: [])
        for w in words: # calc the difference of each word, and put into hmp for quick lookup
            arr = []
            for i in range(1, len(w)):
                arr.append( ord(w[i])  - ord(w[i-1]) )
            hmp[tuple(arr)].append(w) 
        
        for k, v in hmp.items():
            if len(v) == 1:
                return hmp[k][0]
        

