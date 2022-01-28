class WordDictionary:

    def __init__(self):
        self.trie = {} 

    def addWord(self, word: str) -> None: #build the trie
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {} 
            curr = curr[c]
        curr['#'] = {}
        
    
    def search(self, word: str) -> bool:
        def helper(trie, arr):
            if arr:
                if arr[0] in trie:
                    return helper(trie[arr[0]], arr[1:])
                elif arr[0] == '.':
                    for k in trie.keys(): #need to check all the paths
                        if helper(trie[k], arr[1:]) == True: #as long as find a match, return True
                            return True
                else:
                    return False
            else:
                return '#' in trie # check if there's a word ends here

        
        return helper(self.trie, list(word))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# previous approach

# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         if word[0] not in self.trie:
#             self.trie[word[0]] = {}
#         curr = self.trie[word[0]]    
#         for c in word[1:]:
#             if c not in curr:
#                 curr[c] = {}
#             curr = curr[c]
#         curr['$'] = None
    
#     def helper(self, word, hmp):
#         if len(word) == 0:
#             return True if '$' in hmp else False
       
#         i = 0 
#         while i < len(word):
#             if word[i] in hmp:
#                 hmp = hmp[word[i]]
#                 i+=1
#                 if i == len(word):
#                     return True if '$' in hmp else False 
                  
#             else:
#                 if word[i] == ".":
#                     for h in hmp.values():
#                         if h != None and self.helper(word[i+1:], h) == True:
#                             return True
#                     return False 
#                 else:
#                     return False
            
    
    

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """
#         return self.helper(word, self.trie)
    


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)




# RL 20220128: new approach, does not work
# class WordDictionary:

#     def __init__(self):
#         self.trie = {}
        
#     def addWord(self, word: str) -> None:
#         def helper(trie, arr): #using recursive to build the trie
#             if arr:
#                 c = arr[0]
#                 if c not in trie:
#                     trie[c] = {} 
#                 helper(trie[c], arr[1:]) #build the following trie    
#                 if '.' not in trie:
#                     trie['.'] = {}
#                 for k, v in trie[c].items():
#                     if k not in trie['.']:
#                         trie['.'][k] = v
#                 #trie['.'].update(trie[c]) # make the wild card . available in the current trie, pointing the all the leaf from here
#                 # print(arr, trie['.']==trie[c])
#             else:
#                 trie['#'] = None
      
#         helper(self.trie, list(word))
        

#     def search(self, word: str) -> bool:
#         curr = self.trie
#         for c in word:
#             if c not in curr:
#                 return False
#             curr = curr[c]
#         print(self.trie['r']['.']['n'])
#         return '#' in curr #if there's a word ends here
        


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)



# previous approach

# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         if word[0] not in self.trie:
#             self.trie[word[0]] = {}
#         curr = self.trie[word[0]]
#         for c in word[1:]:
#             if c not in curr:
#                 curr[c] = {}
#             curr = curr[c]
#         curr['$'] = None

#     def helper(self, word, hmp):
#         if len(word) == 0:
#             return True if '$' in hmp else False

#         i = 0
#         while i < len(word):
#             if word[i] in hmp:
#                 hmp = hmp[word[i]]
#                 i += 1
#                 if i == len(word):
#                     return True if '$' in hmp else False

#             else:
#                 if word[i] == ".":
#                     for h in hmp.values():
#                         if h != None and self.helper(word[i + 1:], h) == True:
#                             return True
#                     return False
#                 else:
#                     return False

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """
#         return self.helper(word, self.trie)

# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)




# previous approach

# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         if word[0] not in self.trie:
#             self.trie[word[0]] = {}
#         curr = self.trie[word[0]]
#         for i in range(1, len(word)):
#             if word[i] not in curr:
#                 curr[word[i]] = {} 
#             curr = curr[word[i]] 
#         curr[0] = None #end of a path

#     def helper(self, curr, trie):
#         if trie == None:
#             return False
#         elif curr == "":
#             return 0 in trie                
#         local_trie = trie
#         for i in range(len(curr)):
#             c = curr[i]
#             if c != ".":
#                 if c not in local_trie:
#                     return False
#                 else:
#                     local_trie = local_trie[c]
#             elif c==".": #to test each key
#                 if local_trie == None : return False
#                 for k in local_trie.keys():
#                     if self.helper(curr[i+1:], local_trie[k]) == True:
#                         return True
#                 return False 
#         return 0 in local_trie

   
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """ 
#         return self.helper(word, self.trie)



# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)