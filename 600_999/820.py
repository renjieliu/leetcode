class Solution:
    def minimumLengthEncoding(self, words: 'List[str]') -> int:
        ref = set() #Suffix tree, to check if current word is a suffix of the previous words
        words.sort(key = lambda x: len(x), reverse = True)
        output = 0
        for w in words:
            if w not in ref:
                output += (len(w)+1)
                for i in range(len(w)):
                    ref.add(w[i:])
        return output

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
