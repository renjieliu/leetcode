# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(node, curr):  # curr is curr path
            if node:
                if node.left == node.right == None:
                    return curr
                else:
                    if node.left != None:
                        curr.append(node.left.val)
                        dfs(node.left, curr)
                    else:
                        curr.append(None)

                    if node.right != None:
                        curr.append(node.right.val)
                        dfs(node.right, curr)
                    else:
                        curr.append(None)

        if p == None and q == None:
            return True
        elif p != None and q != None:
            curr_1 = [p.val]
            dfs(p, curr_1)
            curr_2 = [q.val]
            dfs(q, curr_2)
            return True if curr_1 == curr_2 else False
        else:
            return False  # p!=None, q==None or vice versa
