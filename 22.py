class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        def helper(output, curr, left, right, n):
            if len(curr) == 2 * n:
                output.append(curr)
            else:
                if left < n:  # keep adding the left
                    helper(output, curr + '(', left + 1, right, n)
                if right < left:  # when above finishes, backtrack to the time when left is < n, and add one right
                    helper(output, curr + ')', left, right + 1, n)

        output = []
        helper(output, "", 0, 0, n)
        return output