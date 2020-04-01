# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def flat(node, pos, curr, output):
            if node.left == node.right == None:
                output.append(curr + [pos])
            else:
                if node.left != None: flat(node.left, 2 * pos, curr + [pos], output)
                if node.right != None: flat(node.right, 2 * pos + 1, curr + [pos], output)

        if root == None: return 0
        output = []
        flat(root, 1, [], output)
        if len(output) == 1: return len(output[0]) - 1
        ans = 0
        for i in range(len(output)):
            for j in range(i + 1, len(output)):
                curr = output[i].copy()
                compare = output[j].copy()
                while curr and compare and curr[0] == compare[
                    0]:  # remove the common path, the rest is the real path. edges =  left_cnt+1-1 + right_cnt+1-1
                    curr.pop(0)
                    compare.pop(0)
                ans = max(ans, len(curr) + 1 - 1 + len(compare) + 1 - 1, len(output[i]) - 1,
                          len(output[j]) - 1)  # plus the common node, and the edges is the nodes -1
                # print(ans, output[i], output[j])
        return ans


