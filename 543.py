# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def compare(c1, c2):
            A = c1.copy()
            B = c2.copy()
            while A and B and A[0] == B[0]:
                A.pop(0)
                B.pop(0)
            return len(A) + len(B)

        def dfs(node, pos, curr, output, ans):
            if node.left == node.right == None:
                if output:
                    maxx = -float('inf')
                    for i in output:
                        maxx = max(maxx, compare(curr + [pos], i), len(curr + [pos]) - 1)
                    ans.append(maxx)
                output.append(curr + [pos])
            else:
                if node.left:
                    dfs(node.left, 2 * pos + 1, curr + [pos], output, ans)
                if node.right:
                    dfs(node.right, 2 * pos + 2, curr + [pos], output, ans)

        if root == None: return 0
        output = []
        ans = []
        dfs(root, 0, [], output, ans)
        return max(ans) if ans else len(output[0]) - 1
