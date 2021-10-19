class Trie:

    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        if '#' not in curr: #mark the end of the word
            curr['#'] = None




    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return '#' in curr



    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# previous approach
# class Trie:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         currTrie = self.trie
#         for c in word:
#             if c not in currTrie:
#                 currTrie[c] = {}
#             currTrie = currTrie[c]
#         currTrie[0] = None  # word end flag
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         currTrie = self.trie
#         for c in word:
#             if c in currTrie:
#                 currTrie = currTrie[c]
#             else:
#                 return False
#         return True if 0 in currTrie else False
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         currTrie = self.trie
#         for c in prefix:
#             if c in currTrie:
#                 currTrie = currTrie[c]
#             else:
#                 return False
#         return True
#
# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)


