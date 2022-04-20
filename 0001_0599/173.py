# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: 'Optional[TreeNode]'): #O(N | N)
        def flat(root): #flat the tree to arr 
            return flat(root.left) + [root.val] + flat(root.right) if root else []
        self.arr = flat(root) 
        self.ptr = 0
        

    def next(self) -> int:
        res = self.arr[self.ptr]
        self.ptr+=1
        return res
        

    def hasNext(self) -> bool:
        return self.ptr < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()




# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         self.tree = []

#         def flat(tree, node):
#             if node.left == node.right == None:
#                 tree.append(node.val)
#             else:
#                 if node.left:
#                     flat(tree, node.left)
#                     tree.append(node.val)
#                 if node.right:
#                     if node.left == None:
#                         tree.append(node.val)
#                     flat(tree, node.right)

#         flat(self.tree, root)
#         self.ptr = -1  # initialize the pointer at the position -1, when call "next", it will move to the head of the tree

#     def next(self) -> int:
#         self.ptr += 1
#         return self.tree[self.ptr]

#     def hasNext(self) -> bool:
#         return self.ptr < len(self.tree) - 1

# # Your BSTIterator object will be instantiated and called as such:
# # obj = BSTIterator(root)
# # param_1 = obj.next()
# # param_2 = obj.hasNext()



