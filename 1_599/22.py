class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        left = n
        def helper(output, curr, left, right):
            if left == 0:
                output.append(curr+")"*right)
            else:
                helper(output, curr + "(", left - 1, right+1)
                if right > 0:
                    helper(output, curr+")", left, right-1)
        output =[]
        helper(output, "", n, 0)
        return output

# previous approach
# class Solution:
#     def generateParenthesis(self, n: int) -> 'List[str]':
#         def helper(output, curr, left, right, n):
#             if len(curr) == 2 * n:
#                 output.append(curr)
#             else:
#                 if left < n:  # keep adding the left
#                     helper(output, curr + '(', left + 1, right, n)
#                 if right < left:  # when above finishes, backtrack to the time when left is < n, and add one right
#                     helper(output, curr + ')', left, right + 1, n)
#
#         output = []
#         helper(output, "", 0, 0, n)
#         return output