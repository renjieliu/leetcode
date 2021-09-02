# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> 'List[Optional[TreeNode]]':
        if n == 1:
            return [TreeNode(1)]
        arr = list(range(1, n+1))
        def helper(output, arr, level):
            if len(arr) == 1:
                return [TreeNode(arr[0])]
            else:
                res = []
                for i in range(len(arr)):
                    leftsub = []
                    L = helper(output, arr[:i], level+1)
                    R = helper(output, arr[i+1:], level+1)
                    if L == []:
                        leftsub.append(TreeNode(arr[i]))
                    else:
                        for leftTree in L:
                            node = TreeNode(arr[i])
                            node.left = leftTree
                            leftsub.append(node)

                    if R == []:
                        res += leftsub
                    else:
                        for node in leftsub:
                            for rightTree in R:
                                NewNode = TreeNode(node.val)
                                NewNode.left = node.left
                                NewNode.right = rightTree
                                res.append(NewNode)
                                #print(res, level)

                    if level == 0:
                        output += res
                        #print(arr[i],'output, ', output)
                        res = []

                if level !=0:
                    return res

        output = []
        helper(output, arr, 0)
        return list(set(output))
