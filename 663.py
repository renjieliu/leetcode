# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkEqualTree(self, root: 'Optional[TreeNode]') -> bool:
        def dfs(total, hmp, node, idx):  # to calculate the total sum of the entire tree, and sum of each subtree
            if node.left == node.right == None:
                hmp[idx] = [0, 0]  # left sub, right sub
                total[0] += node.val
                return node.val
            else:
                total[0] += node.val
                left = right = 0
                if node.left:
                    left = dfs(total, hmp, node.left, idx * 2 + 1)
                if node.right:
                    right = dfs(total, hmp, node.right, idx * 2 + 2)
                hmp[idx] = [left, right]
                return left + right + node.val

        def cut(total, hmp, node, idx):
            if node.left == node.right == None:
                return False
            else:
                if node.left:
                    if total == 2 * hmp[idx][0]:  # total == 2*sum(left subtree), it can be split from left edge
                        return True
                    else:
                        res = cut(total, hmp, node.left, idx * 2 + 1)
                        if res == True:
                            return True
                if node.right:
                    if total == 2 * hmp[idx][1]:  # total == 2*sum(right) subtree), it can be split from right edge
                        return True
                    else:
                        res = cut(total, hmp, node.right, idx * 2 + 2)
                        if res == True:
                            return True
                return False

        hmp = {}
        total = [0]
        dfs(total, hmp, root, 0)
        total = total[0]
        # print(hmp)
        return cut(total, hmp, root, 0)





















