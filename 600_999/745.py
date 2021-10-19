Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]

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

