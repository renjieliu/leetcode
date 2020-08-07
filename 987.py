# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> 'List[List[int]]':
        def dfs(hmp, index, level, node):
            if node.left == node.right == None:
                position = (index[0], index[1], level)
                if position not in hmp:
                    hmp[position] = []
                hmp[position].append(node.val)
            else:
                position = (index[0], index[1], level)
                if position not in hmp:
                    hmp[position] = []
                hmp[position].append(node.val)
                if node.left:
                    dfs(hmp, [index[0] - 1, index[1] - 1], level + 1, node.left)
                if node.right:
                    dfs(hmp, [index[0] + 1, index[1] - 1], level + 1, node.right)

        hmp = {}
        dfs(hmp, [0, 0], 0, root)
        k_list = sorted(hmp.keys(), key=lambda x: x[1], reverse=True)  # sorted by y
        k_list = sorted(k_list, key=lambda x: x[0])  # sort by x
        # print(k_list)

        output = []
        prev = k_list[0][0]
        temp = sorted(hmp[k_list[0]])  # sort by the values
        for k in k_list[1:]:
            if k[0] == prev:
                temp += sorted(hmp[k])
            else:
                output.append(temp)
                temp = sorted(hmp[k])
                prev = k[0]

        output.append(temp)
        return output














