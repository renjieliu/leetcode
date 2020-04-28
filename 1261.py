# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.tree = []
        node = root

        def flat(tree, index, node):
            if node.left == node.right == None:
                tree.append(index)
            else:
                tree.append(index)
                if node.left: flat(tree, 2 * index + 1, node.left)
                if node.right: flat(tree, 2 * index + 2, node.right)

        flat(self.tree, 0, node)

    def find(self, target: int) -> bool:
        return target in self.tree

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)