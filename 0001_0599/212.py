class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]': # RL 20221105: Copied solution, O( M*(4*3**(L-1)) | N )
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    



# my previous accepted solution, TLE on 2022-11-05

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: # O( MN | MN )
#         trie = {} 
#         for w in words:
#             curr = trie
#             for c in w:
#                 if c not in curr:
#                     curr[c] = {}
#                 curr = curr[c]
#             curr['#'] = None # flag the end of one word
        
#         def dfs(output, trie, path, board, r, c, seen):
#             curr = trie[board[r][c]]
#             if '#' in curr: #it has reach the end of one word
#                 output.append(path)
#                 del curr['#'] #take out the word from the trie
            
#             direction = [[1,0], [0,1], [-1,0], [0,-1]]
#             for a, b in direction:
#                 if -1<r+a<len(board) and -1<c+b<len(board[0]) and ((r+a), (c+b)) not in seen and board[r+a][c+b] in curr:
#                     seen.add((r+a, c+b))
#                     dfs(output, curr, path+board[r+a][c+b], board, r+a, c+b, seen)
#                     seen.remove((r+a, c+b))
        
#         output = []
#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 if board[r][c] in trie:
#                     dfs(output, trie, board[r][c], board, r, c, {(r,c)})
        
#         return output
            
            
            
            



# previous solution

# class Solution:
#     def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
#         trie = {}
#         for w in words:
#             curr = trie
#             for c in w:
#                 if c not in curr:
#                     curr[c] = {}
#                 curr = curr[c]
#             curr['#'] = None  # flag the end of one word

#         def dfs(output, trie, path, board, r, c, seen):
#             curr = trie[board[r][c]]
#             if '#' in curr:  # it has reach the end of one word
#                 output.append(path)
#                 del curr['#']  # take out the word from the trie

#             direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#             for a, b in direction:
#                 if -1 < r + a < len(board) and -1 < c + b < len(board[0]) and ((r + a), (c + b)) not in seen and \
#                         board[r + a][c + b] in curr:
#                     seen.add((r + a, c + b))
#                     dfs(output, curr, path + board[r + a][c + b], board, r + a, c + b, seen)
#                     seen.remove((r + a, c + b))

#         output = []
#         for r in range(
#                 len(board)):  # if current is in the trie, search the neighbour, check if they are in the trie as well.
#             for c in range(len(board[0])):
#                 if board[r][c] in trie:
#                     dfs(output, trie, board[r][c], board, r, c, {(r, c)})
#         return output



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