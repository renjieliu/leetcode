class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        end = '$'
        trie = {}
        for w in words:
            curr = trie
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr[end] = w  # use the word as the value for the last $

        def dfs(row, col, parent, matchedWords):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop('$', False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '`seen`'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                r, c = row + rowOffset, col + colOffset
                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] not in currNode:
                    continue
                else:
                    dfs(r, c, currNode, matchedWords)
            # restore
            board[row][col] = letter

            # # Optimization: incrementally remove the matched leaf node in Trie.
            # if not currNode:
            #     parent.pop(letter)

        matchedWords = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie:
                    dfs(r, c, trie, matchedWords)

        return matchedWords



# previous approach
# class Solution:
#     def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
#         end = '$'
#         trie = {}
#         for w in words:
#             curr = trie
#             for c in w:
#                 if c not in curr:
#                     curr[c] = {}
#                 curr = curr[c]
#             curr[end] = w  # use the word as the value for the last $
#
#         def dfs(row, col, parent, matchedWords):
#
#             letter = board[row][col]
#             currNode = parent[letter]
#
#             # check if we find a match of word
#             word_match = currNode.pop('$', False)
#             if word_match:
#                 # also we removed the matched word to avoid duplicates,
#                 #   as well as avoiding using set() for results.
#                 matchedWords.append(word_match)
#
#             # Before the EXPLORATION, mark the cell as visited
#             board[row][col] = '`seen`'
#
#             # Explore the neighbors in 4 directions, i.e. up, right, down, left
#             for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                 r, c = row + rowOffset, col + colOffset
#                 if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] not in currNode:
#                     continue
#                 else:
#                     dfs(r, c, currNode, matchedWords)
#             # restore
#             board[row][col] = letter
#
#             # # Optimization: incrementally remove the matched leaf node in Trie.
#             # if not currNode:
#             #     parent.pop(letter)
#
#         matchedWords = []
#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 if board[r][c] in trie:
#                     dfs(r, c, trie, matchedWords)
#
#         return matchedWords
#
#
#
