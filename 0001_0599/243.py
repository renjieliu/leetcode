class Solution:
    def shortestDistance(self, words: 'List[str]', word1: str, word2: str) -> int:
        A = []
        B = []
        for i, w in enumerate(words):
            if w == word1:
                A.append(i)
            elif w == word2:
                B.append(i)
        output = float('inf')

        while A and B:  # compare the first element
            while A and B and A[0] < B[0]:
                output = min(output, abs(A[0] - B[0]))
                A.pop(0)
            while A and B and B[0] < A[0]:
                output = min(output, abs(A[0] - B[0]))
                B.pop(0)

        return output


# previous approach
# class Solution:
#     def shortestDistance(self, words: 'List[str]', word1: str, word2: str) -> int:
#         hmp = {}
#         i = 0
#         while i < len(words):
#             if words[i] not in hmp:
#                 hmp[words[i]] = []
#             hmp[words[i]].append(i)
#             i += 1
#         output = float('inf')
#         while hmp[word1] and hmp[word2]:
#             output = min(output, abs(hmp[word1][0] - hmp[word2][0]))
#             if hmp[word1][0] < hmp[word2][0]:
#                 hmp[word1].pop(0)
#             else:
#                 hmp[word2].pop(0)
#         return output
