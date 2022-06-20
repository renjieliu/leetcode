class Solution:
    def minimumLengthEncoding(self, words: 'List[str]') -> int: #O( N*K | N*K), K being the length of the longest word
        trie = {}
        seen = []
        for w in set(words):
            curr = trie
            for c in w[::-1]:
                curr[c] = curr.get(c, {})
                curr = curr[c]
            seen.append([curr,  len(w) + 1]) # current trie, len(curr) is to check if the trie has children
        # print(seen)
        return sum(leaf for currTrie, leaf in seen if len(currTrie) == 0) #len(currTrie) == 0, no children, therefore, current word is not a suffix of any other word
    


# previous solution

# class Solution:
#     def minimumLengthEncoding(self, words: 'List[str]') -> int:
#         ref = set() #Suffix tree, to check if current word is a suffix of the previous words
#         words.sort(key = lambda x: len(x), reverse = True)
#         output = 0
#         for w in words:
#             if w not in ref:
#                 output += (len(w)+1)
#                 for i in range(len(w)):
#                     ref.add(w[i:])
#         return output

# previous approach
# class Solution:
#     def minimumLengthEncoding(self, words: 'List[str]') -> int:
#         words.sort(key=lambda x: len(x))
#         curr = ""
#         for i in range(len(words)):  # check each words, see if it's a tail of others
#             good = 1
#             for j in range(i + 1, len(words)):
#                 # print(words[i], words[j], isTail(words[i], words[j]))
#                 a = words[i]
#                 b = words[j]
#                 if b[-len(a):] == a:
#                     good = 0
#                     break
#             if good == 1:
#                 curr += words[i] + '#'
#
#         # print(curr)
#         return len(curr)
