# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root == None: return ""
        hmp = {}

        def flat(node, hmp, idx):
            if node:
                hmp[idx] = node.val
            if node.left:
                flat(node.left, hmp, 2 * idx + 1)
            if node.right:
                flat(node.right, hmp, 2 * idx + 2)

        flat(root, hmp, 0)
        output = ""
        for k, v in hmp.items():
            output += str(k) + ":" + str(v) + "-"
        return output[:-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "": return None
        arr = data.split('-')
        hmp = {}
        for a in arr:
            b = a.split(':')
            hmp[int(b[0])] = int(b[1])
        root = TreeNode(hmp[0])

        def build(arr, node, curr_idx):
            left = 2 * curr_idx + 1
            if left in hmp:
                node.left = TreeNode(hmp[left])
                build(arr, node.left, left)

            right = 2 * curr_idx + 2
            if right in hmp:
                node.right = TreeNode(hmp[right])
                build(arr, node.right, right)

        build(arr, root, 0)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans