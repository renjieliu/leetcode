class StreamChecker:

    def __init__(self, words: 'List[str]'):
        self.trie = {} 
        self.stk = deque()
        for w in words:
            w = w[::-1]
            if w[0] not in self.trie:
                self.trie[w[0]] = {}
            curr = self.trie
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['$'] = None 

    def query(self, letter: str) -> bool:
        self.stk.appendleft(letter)
        node = self.trie
        for c in self.stk:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '$' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)



# previous approach
# class StreamChecker:

#     def __init__(self, words: 'List[str]'):
#         self.trie = {}
#         self.stk = deque()
#         for w in words: #build the trie reversely
#             w = w[::-1]
#             if w[0] not in self.trie:
#                 self.trie[w[0]] = {}
#             curr = self.trie
#             for c in w:
#                 if c not in curr:
#                     curr[c] = {}
#                 curr = curr[c]
#             curr['$'] = None

#     def query(self, letter: str) -> bool:
#         self.stk.appendleft(letter) #add current letter to the start of the queue.
#         node = self.trie
#         for c in self.stk:
#             if '$' in node:
#                 return True
#             if c not in node:
#                 return False
#             node = node[c]
#         return '$' in node


# # Your StreamChecker object will be instantiated and called as such:
# # obj = StreamChecker(words)
# # param_1 = obj.query(letter)