class Solution:
    def suggestedProducts(self, products: 'List[str]', searchWord: str) -> 'List[List[str]]': #O( K*N | K*N ) K is the length of the longest word
        products.sort() #sort the products, to avoid sorting when retrieving
        trie = {} 
        for i, p in enumerate(products):
            curr = trie
            for c in p:
                if c not in curr:
                    curr[c] = {}
                    curr[c]['word'] = []
                curr[c]['word'].append(p)
                curr = curr[c]
        
        def helper(trie, word): #to get the list of products in the trie, with word
            curr = trie
            for i, c in enumerate(word):
                if c not in curr:
                    return []
                curr = curr[c]
            return curr['word'][:3]
        
        
        output = []
        for i in range(len(searchWord)):
            output.append(helper(trie, searchWord[:i+1]))
        return output
    


# previous solution

# class Solution:
#     def suggestedProducts(self, products: 'List[str]', searchWord: str) -> 'List[List[str]]':
#         trie = {}
#         products.sort()  # no need to sort the trie. sort the products list, the result will be sorted as well.
#         for p in products:
#             curr = trie
#             for c in p:
#                 if c not in curr:
#                     curr[c] = [{}, []]  # [newTrie, word]
#                 curr[c][1].append(p)
#                 curr = curr[c][0]

#         #         def orderTrie(trie): #sort the value of trie
#         #             for k, v in trie.items():
#         #                 v[1].sort()
#         #                 orderTrie(v[0])

#         #         orderTrie(trie)
#         output = []
#         curr = trie
#         for i, c in enumerate(searchWord):
#             if c in curr:
#                 if len(curr[c][1]) > 3:
#                     output.append(curr[c][1][:3])
#                 else:
#                     output.append(curr[c][1])
#                 curr = curr[c][0]
#             else:  # for the rest of the word, just add [] to output
#                 for j in range(i, len(searchWord)):
#                     output.append([])
#                 break

#         return output


# previous approach
# class Solution:
#     def suggestedProducts(self, products: 'List[str]', searchWord: str) -> 'List[List[str]]':
#         trie = {}
#         for p in products:
#             curr = trie
#             for c in p:
#                 if c not in curr:
#                     curr[c] = [{}, []]  # [newTrie, word]
#                 curr[c][1].append(p)
#                 curr = curr[c][0]
#
#         def orderTrie(trie):  # sort the value of trie
#             for k, v in trie.items():
#                 v[1].sort()
#                 orderTrie(v[0])
#
#         orderTrie(trie)
#         output = []
#         curr = trie
#         for i, c in enumerate(searchWord):
#             if c in curr:
#                 if len(curr[c][1]) > 3:
#                     output.append(curr[c][1][:3])
#                 else:
#                     output.append(curr[c][1])
#                 curr = curr[c][0]
#             else:  # for the rest of the word, just add [] to output
#                 for j in range(i, len(searchWord)):
#                     output.append([])
#                 break
#
#         return output
#
#
