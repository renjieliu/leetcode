# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ptr = -1
        self.arr = []

        def flat(node, arr):
            if node.left == node.right == None:
                arr.append(node.val)
            else:
                arr.append(node.val)
                if node.left:
                    flat(node.left, arr)
                if node.right:
                    flat(node.right, arr)

        if root != None:
            flat(root, self.arr)
        self.arr.sort()

    def hasNext(self) -> bool:
        return self.ptr < len(self.arr) - 1

    def next(self) -> int:
        self.ptr += 1
        return self.arr[self.ptr]

    def hasPrev(self) -> bool:
        return self.ptr > 0

    def prev(self) -> int:
        self.ptr -= 1
        return self.arr[self.ptr]

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()