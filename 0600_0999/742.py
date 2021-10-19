# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def steps2root(A, B):
            output = -1
            while A and B and A[0] == B[0]:
                A.pop(0)
                B.pop(0)
                output += 1
            return output

        def dfs(output, curr, node):
            if node.left == node.right == None:
                output.append(curr + [node.val])
            else:
                if node.left != None:
                    dfs(output, curr + [node.val], node.left)
                if node.right != None:
                    dfs(output, curr + [node.val], node.right)

        output = []
        dfs(output, [], root)
        leaf = []
        distance = level = ans = stop = -1
        for i in range(len(output)):
            o = output[i]
            if k in o:
                level = o.index(k)
                distance = len(o) - 1 - level
                ans = o[-1]
                stop = i
                break
        for curr in output[:stop] + output[
                                    stop + 1:]:  # check if the closest is on the same tree or need go to the root and move to the leaf of the other tree
            back = steps2root(output[stop][:level + 1].copy(), curr.copy())
            currBack = len(curr) - 1 - back  # how many steps to go back to the same root
            compareback = level - back
            if compareback + currBack < distance:
                ans = curr[-1]
                distance = compareback + currBack

        return ans