# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def buildDict(node, idx, hmp, prnt_kid):
            if node.left == node.right == None:
                hmp[idx] = node.val
            else:
                hmp[idx] = node.val
                prnt_kid[idx] = []
                if node.left:
                    prnt_kid[idx].append(idx * 2 + 1)
                    buildDict(node.left, idx * 2 + 1, hmp, prnt_kid)
                if node.right:
                    prnt_kid[idx].append(idx * 2 + 2)
                    buildDict(node.right, idx * 2 + 2, hmp, prnt_kid)

        def sumKids(prnt_kid, k, output):
            path1 = path2 = None
            res = 0
            if len(prnt_kid[k]) == 1:
                leaf = prnt_kid[k][0]
                if leaf in prnt_kid:
                    path1 = sumKids(prnt_kid, leaf, output)
                else:
                    path1 = hmp[leaf]
                    output[-1] = max(output[-1], path1)
            elif len(prnt_kid[k]) == 2:
                leaf_1 = prnt_kid[k][0]
                leaf_2 = prnt_kid[k][1]
                if leaf_1 in prnt_kid:
                    path1 = sumKids(prnt_kid, leaf_1, output)
                else:
                    path1 = hmp[leaf_1]
                    output[-1] = max(output[-1], path1)

                if leaf_2 in prnt_kid:
                    path2 = sumKids(prnt_kid, leaf_2, output)
                else:
                    path2 = hmp[leaf_2]
                    output[-1] = max(output[-1], path2)

            if path2 != None:
                output[-1] = max(output[-1], hmp[k] + path1, hmp[k] + path2, hmp[k] + path1 + path2, hmp[k])
                # print(k, output)
                return max(hmp[k] + path1, hmp[k] + path2, hmp[k])

            else:
                output[-1] = max(output[-1], hmp[k] + path1, hmp[k])
                # print(k, output)
                return max(hmp[k] + path1, hmp[k])

        if root == None:
            return 0
        else:
            hmp = {}  # to store the value for each position
            prnt_kid = {}
            path = []
            buildDict(root, 0, hmp, prnt_kid)

            output = [-float('inf')]
            if 0 in prnt_kid:
                sumKids(prnt_kid, 0, output)  # start at 0
                return output[-1]
            else:  # only root in the tree
                return hmp[0]











