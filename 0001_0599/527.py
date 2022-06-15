class Solution:
    def wordsAbbreviation(self, words: 'List[str]') -> 'List[str]': # O(N**2 | N)
        hmp = {} #store the final abbreviation of the word
        def helper(hmp, arr, firstN): # taking the firstN for each word, and abbrev.
            abbr = defaultdict(lambda: []) # store the temp abbreviation of the word
            for w in arr:
                if len(w) <= 3:
                    abbr[w].append(w)
                else:
                    rem = len(w)-1 - firstN #total length - last character - firstTaken
                    A = w[:firstN] + str(rem) + w[-1]
                    if len(A) == len(w): #cannot shorten
                        abbr[w].append(w)
                    else:
                        abbr[A].append(w)
            
            keyList = list(abbr.keys())
            for k in keyList:
                if len(abbr[k]) == 1: #unique abbreviation
                    hmp[abbr[k][0]] = k 
                else:  # if not unique, keep taking more characters from first
                    helper(hmp, abbr[k], firstN+1)
                
                del abbr[k]
        
        helper(hmp, words, 1)
        output = []
        for w in words:
            output.append(hmp[w])
        return output
        
        
            
