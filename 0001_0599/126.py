class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: 'List[str]') -> 'List[List[str]]': # RL 20220813 copied solution, O(NK**2 + P | NK), N is the length of the wordList, K is the length of the beginWord, P is possible ways to reach endWord 
        #generate adjacent list
        Nei = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                Nei[pattern].append(word)     
        
        #breadth first search + generate parent dictionary with path length limit
        seen = {beginWord:0}
        q = deque([(beginWord,0)])
        minDist = float("inf")
        Parent = defaultdict(set)
        while q:        
            for _ in range(len(q)):
                pre,dis = q.popleft()
                for i in range(len(pre)):
                    pattern = pre[:i] + "*" + pre[i+1:]
                    for neighbor in Nei[pattern]:
                        if neighbor not in seen or (seen[neighbor] == dis + 1 and seen[neighbor] <= minDist):
                            if neighbor == endWord: 
                                minDist = dis + 1
                            Parent[neighbor].add(pre)
                            if neighbor not in seen:   
                                q.append((neighbor,dis+1))
                                seen[neighbor] = dis + 1
								
        #generate path from parent dictionary
        def makeList(cur,Path):
            if cur == beginWord:
                res.append(Path)
            else:
                for parent in Parent[cur]:
                    makeList(parent,[parent] + Path)
        res = []
        makeList(endWord,[endWord])
        
        #return results
        return res


    
    
# my solution, TLE / MLE 
    
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]: # 20220813, my approach, TLE,  #O( N * L | N * L) N = len(wordList), L = len(beginWord)
#         output = []
#         mask = {}
#         for i in range(len(beginWord)): #mask all the possibilities for the beginWord
#             curr = beginWord[:i] +  "*" + beginWord[i+1:]
#             if curr not in mask:
#                 mask[curr] = []
#             mask[curr].append(beginWord)

#         for w in wordList: # mask all the words in the wordList
#             for i in range(len(w)):
#                 curr = w[:i] + "*" + w[i+1:]
#                 if curr not in mask:
#                     mask[curr] = []
#                 mask[curr].append(w)
#         stk = [ [{beginWord}, [beginWord] ] ]  # [[path]]
#         while stk:
#             if output:
#                 return output
#             nxt = []
#             while stk:
#                 currSet, currPath = stk.pop() 
#                 currSet = currSet.copy()

#                 lastWord = currPath[-1] #last word in the path
                
#                 if lastWord == endWord: # if it's same as the endWord, add the path to the output
#                     output.append(currPath) # take out the first lookup set
#                 else:
#                     for i in range(len(lastWord)):
#                         currMask = lastWord[:i] + "*" + lastWord[i+1:]
#                         if currMask in mask:
#                             for w in mask[currMask]:
#                                 if w not in currSet: #the word is not seen in the current group
#                                     currSet.add(w)
#                                     nxt.append ( [currSet, currPath + [w] ] )

#             stk = nxt
#             print(len(stk))
#         return output
    




# previous solution

# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: 'List[str]') -> 'List[List[str]]':
#         wordSet = set(wordList)  # to check if a word is existed in O(1)

#         def neighbors(word):
#             for i in range(len(word)):  # change every possible single letters and check if it's in wordSet
#                 for c in ascii_lowercase:
#                     newWord = word[:i] + c + word[i + 1:]
#                     if newWord in wordSet:
#                         yield newWord

#         layer = {}
#         layer[beginWord] = [[beginWord]]  # layer[word] is all possible sequence paths which start from beginWord and end at `word`.
#         while layer.keys():
#             nextLayer = defaultdict(list)
#             for word in layer.keys():
#                 if word == endWord:
#                     return layer[word]  # return all shortest sequence paths
#                 for nei in neighbors(word):
#                     for path in layer[word]:
#                         nextLayer[nei].append(path + [nei])  # add new word to all sequences and form new layer element
#             wordSet -= set(nextLayer.keys())  # remove visited words to prevent loops
#             layer = nextLayer  # move to new layer

#         return []

