class Solution:
    def validWordSquare(self, words: 'List[str]') -> bool:
        for r in range(len(words)):
            for c in range(len(words[r])):
                curr = words[r][c]
                pivot_r = c
                pivot_c = r
                if pivot_r >= len(words) or pivot_c >= len(words[pivot_r]) or curr != words[pivot_r][pivot_c]:
                    return False
        return True
