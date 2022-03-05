class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        hmp = {} 
        for w in wordList:
            for i in range(len(w)): #build pattern for each position of each word
                pattern = w[:i] + "*" + w[i+1:]
                if pattern not in hmp:
                    hmp[pattern] = []
                hmp[pattern].append(w)

        stk = [beginWord]
        step = 0 
        while stk: #construct the pattern for each word at each position, and find the next possible word
            nxt = []
            step += 1
            while stk:
                w = stk.pop()
                if w == endWord:
                    return step
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i+1:]
                    if pattern in hmp:
                        nxt += hmp[pattern]
                        del hmp[pattern]
                        
            stk = nxt
        return 0
    

# pvevious approach

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
#         hmp = {}
#         L = len(beginWord)
#         for w in wordList: #put mask at each location of each word,to answer the question = what can become current word
#             for i in range(L):
#                 mask = w[:i] + "*" + w[i+1:]
#                 if w[:i] + "*" + w[i+1:] not in hmp:
#                     hmp[mask] = []
#                 hmp[mask].append(w)
        
#         step = 0
#         stk = [beginWord]
#         while stk:
#             nxt = []
#             step += 1
#             while stk:
#                 curr = stk.pop()
#                 if curr == endWord:
#                     return step
#                 else:
#                     for i in range(L): # to answer the question - what's the word can current word turn into?
#                         mask = curr[:i] + "*" + curr[i+1:]
#                         if mask in hmp:
#                             nxt += hmp[mask]
#                             del hmp[mask]
#             stk = nxt
        
#         return 0
       
                


# previous approach

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
#         if endWord not in wordList: return 0
#         hmp = {}
#         for w in wordList:
#             for i in range(len(w)): #all the possible candidates
#                 if w[:i] + '*' + w[i+1:] not in hmp:
#                     hmp[w[:i] + '*' + w[i+1:]] = []
#                 hmp[w[:i] + '*' + w[i+1:]].append(w)

#         layer = 1
#         stk = [beginWord]
#         run = 1
#         while run == 1 :
#             nxt = []
#             while stk:
#                 curr = stk.pop(0)
#                 if curr == endWord:
#                     return layer
#                 for i in range(len(curr)):
#                     mask = curr[:i] + '*' + curr[i+1:] #all the possible candidates derived from current word
#                     if mask in hmp:
#                         nxt += hmp[mask] # next round of check
#                         del hmp[mask]
#             layer += 1
#             stk = nxt
#             if stk == []:
#                 run = 0

#         return 0


