# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def dfs(path, node):  # this is to find the path lead to the node - output format: from node to root
            if node.parent == None:
                path.append(node)
            else:
                path.append(node)
                dfs(path, node.parent)

        def compare(arr1, arr2):
            if arr1[0] != arr2[0]:  # if the root node is not the same, no need to compare anymore
                return None
            output = arr1[0]
            while arr1 and arr2:
                A = arr1.pop(0)
                B = arr2.pop(0)
                if A == B:
                    output = A
            return output

        p_up = []
        q_up = []
        dfs(p_up, p)
        dfs(q_up, q)

        return compare(p_up[::-1], q_up[::-1])  # compare from root to bottom



























