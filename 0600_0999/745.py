class WordFilter:

    def __init__(self, words: 'List[str]'): #O(K**2*N | K**2*N) # K is the lengthe of the longest word. N = len(words)
        self.trie = {}
        for i, w in enumerate(words): # for word like "apple", add all the suffix + '#' + prefix to the trie
            w += '#' 
            for j in range(len(w)):
                curr = self.trie
                for k in range(j, 2*len(w)-1): #apple#apple, pple#apple, ple#apple.... #apple
                    char = w[k%len(w)]
                    curr[char] = curr.get(char, {'loc': i})
                    curr[char]["loc"] = i 
                    curr=curr[char]
        
        

    def f(self, pref: str, suff: str) -> int:
        curr = self.trie
        #print(curr)
        word = suff+'#'+ pref
        for c in word:
            if c not in curr:
                return -1
            curr = curr[c]
        return curr["loc"]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)



#previous solution

# class WordFilter:

#     def __init__(self, words: 'List[str]'): # O( N*(K**2) | N*(K**2) ) N is the length of the list, K is the length of the longest word
#         self.trie = {}
#         for i, w in enumerate(words): #for each word, insert all the possible pre + post into the trie
#             w += '#'
#             for j in range(len(w)):
#                 curr = self.trie
#                 curr['idx'] = i #this is to track the current trie word location.
#                 for x in range(j, len(w)*2-1): # for apple, first insert apple#apple, then pple#apple... etc
#                     char = w[x%len(w)]
#                     if char not in curr:
#                         curr[char] = {}
#                     curr[char]['idx'] = i
#                     curr = curr[char]


#     def f(self, prefix: str, suffix: str) -> int:  # O(K | 1) , K is the length of the pre + suffix
#         find = suffix +'#' + prefix #just to find suffix + '#' + prefix in the trie
#         curr = self.trie
#         output = -1
#         for c in find:
#             if c not in curr:
#                 return -1
#             curr = curr[c]
#         return curr['idx']
        
        



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)



# previous solution 

# Trie = lambda: collections.defaultdict(Trie)
# WEIGHT = False

# class WordFilter(object):
#     def __init__(self, words):
#         self.trie = Trie()

#         for weight, word in enumerate(words):
#             word += '#'
#             for i in range(len(word)):
#                 cur = self.trie
#                 cur[WEIGHT] = weight
#                 for j in range(i, 2 * len(word) - 1):
#                     cur = cur[word[j % len(word)]]
#                     cur[WEIGHT] = weight

#     def f(self, prefix, suffix):
#         cur = self.trie
#         for letter in suffix + '#' + prefix:
#             if letter not in cur:
#                 return -1
#             cur = cur[letter]
#         return cur[WEIGHT]

# class WordFilter:

#     def __init__(self, words: List[str]):
#         self.trie_pre = {}
#         self.trie_suffix = {}
#         for pos in range(len(words)):
#             word = words[pos]
#             curr = self.trie_pre
#             for i, c in enumerate(word):
#                 if c not in curr:
#                     curr[c] = [[], {}]
#                 curr[c][0].append(pos)
#                 curr = curr[c][1]

#         for pos in range(len(words)):
#             word = words[pos]
#             curr = self.trie_suffix
#             for i, c in enumerate(word[::-1]):
#                 if c not in curr:
#                     curr[c] = [[], {}]
#                 curr[c][0].append(pos)
#                 curr = curr[c][1]

# #         print (len(self.trie_pre))
# #         print (len(self.trie_suffix))


#     def f(self, prefix: str, suffix: str) -> int:
#         pool_prefix = []
#         pool_suffix = []
#         stk = list(prefix)
#         curr = self.trie_pre
#         while stk:
#             c = stk.pop(0)
#             if c in curr:
#                 pool_prefix = curr[c][0]
#                 curr = curr[c][1]
#             else:
#                 return -1

#         stk = list(suffix)[::-1]
#         curr = self.trie_suffix
#         while stk:
#             c = stk.pop(0)
#             if c in curr:
#                 pool_suffix = curr[c][0]
#                 curr = curr[c][1]
#             else:
#                 return -1

#         #cross = list(set(pool_prefix) & set(pool_suffix))
#         print('pre', pool_prefix)
#         print('suffix', pool_suffix)
#         # #if cross:
#         #     print('pre', pool_prefix)
#         #     print('suffix', pool_suffix)
#         #     return #max(cross)
#         # else:
#         #     return -1

#         #print('pre', pool_prefix)
#         #print('suffix', pool_suffix)

#         while pool_prefix and pool_suffix:
#             if pool_prefix[-1] == pool_suffix[-1]:
#                 return pool_suffix[-1]
#             elif pool_prefix[-1] > pool_suffix[-1]:
#                 pool_prefix.pop()
#             else:
#                 pool_suffix.pop()
#         return -1


# # Your WordFilter object will be instantiated and called as such:
# # obj = WordFilter(words)
# # param_1 = obj.f(prefix,suffix)

