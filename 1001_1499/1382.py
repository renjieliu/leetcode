# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(flat, node):
            if node.left == node.right == None:
                flat.append(node.val)
                return
            else:
                flat.append(node.val)
                if node.left != None:
                    dfs(flat, node.left)
                if node.right != None:
                    dfs(flat, node.right)

        if root == None:
            return None
        else:
            flat = []
            dfs(flat, root)
            flat.sort()

            def buildTree(arr, tree):
                if len(arr) == 0:
                    return
                mid = (len(arr) - 1) // 2
                val = arr[mid]
                if val < tree.val:
                    tree.left = TreeNode(val)
                    buildTree(arr[:mid], tree.left)  # build left tree
                    buildTree(arr[mid + 1:], tree.left)  # build right tree
                elif val > tree.val:
                    tree.right = TreeNode(val)
                    buildTree(arr[:mid], tree.right)  # build left tree
                    buildTree(arr[mid + 1:], tree.right)  # build right tree

            mid = (len(flat) - 1) // 2
            tree = TreeNode(flat[mid])
            buildTree(flat[:mid], tree)
            buildTree(flat[mid + 1:], tree)
            return tree
























